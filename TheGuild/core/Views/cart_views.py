from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from TheGuild.core.Serializers.cart_serializer import CartSerializer
from TheGuild.core.Models.CartModel import Cart
from TheGuild.core.Models.StorageModel import Storage, Storage_Goods
from TheGuild.core.Models.CharacterModel import Character
from TheGuild.core.Models.WorkshopModel import Workshop
from TheGuild.core.Models.GoodsModel import Goods
from TheGuild.core.Models.CountryModel import GridPoint, Country
from datetime import datetime, UTC

class CartListAllView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CartSerializer
    def get_queryset(self):
        carts = Cart.objects.all()
        for cart in carts:
            cart.UpdateCart()
        return carts
    
class CartCountryView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CartSerializer
    
    def get_queryset(self):
        filter = self.kwargs['countryID']
        if filter is not None:
            chars = Character.objects.filter(country_id=filter).values_list('id',  flat=True)
            queryset = Cart.objects.filter(id__in=chars)
            for cart in queryset:
                cart.UpdateCart()
            return queryset
        return None
    
class CartsAtWorkshotView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=CartSerializer
    
    def get_queryset(self):
        workshopID = self.kwargs['workshopID']
        if workshopID is not None:
            workshop = Workshop.objects.get(id=workshopID)
            carts = Cart.objects.filter(character_id=workshop.character.id, location_id=workshopID, is_traveling=False)
            return carts
        return None
    
class WorkshopToCartTransferView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self, request):
        cart_id = request.data["cart_id"]
        workshop_id = request.data["workshop_id"]
        goods_id = request.data["goods_id"]
        quantity = request.data["quantity"]
        if cart_id is None or workshop_id is None:            
            return Response("Cart or Workshop not found", status=status.HTTP_204_NO_CONTENT)
        
        cart = Cart.objects.get(id=cart_id)
        if not cart:
            return Response("Could not find cart", status=status.HTTP_204_NO_CONTENT)
        cart.UpdateCart()
        if cart.location_type.lower() != "workshop" or cart.location_id != workshop_id:
            return Response("This cart is not at the correct location for this task", status=status.HTTP_400_BAD_REQUEST)
        
        workshop = Workshop.objects.get(id=workshop_id)
        try:
            workshop_goods = Storage_Goods.objects.get(storage_id=workshop.storage.id, goods_data_id=goods_id)
        except Exception as error:
            return Response("Could not find goods in workshop" + error,status=status.HTTP_400_BAD_REQUEST) 
        number_of_items_in_cart = Storage_Goods.objects.filter(storage_id=cart.storage.id).count()
        cart_goods = Storage_Goods.objects.get_or_create(storage_id=cart.storage.id, goods_data_id=goods_id)
        if cart_goods[1] and number_of_items_in_cart > cart.storage.number_of_storage_spaces:
            return Response("Not enough space in the cart", status=status.HTTP_400_BAD_REQUEST)
        elif not cart_goods[1] and cart_goods[0].quantity + quantity > cart_goods[0].max_stack_size:
            return Response("Storage space too small", status=status.HTTP_400_BAD_REQUEST)
        workshop_goods.quantity -= quantity
        cart_goods[0].quantity += quantity
        cart_goods[0].save()
        workshop_goods.save()
        return Response("Moved resources to cart " + str(cart_id))
    
class StorageToStorageTransferView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        storage_1_id = request.data["storage_1_id"]
        storage_2_id = request.data["storage_2_id"]
        goods_id = request.data["goods_id"]
        quantity = request.data["quantity"]
        
        if storage_1_id == storage_2_id:
            return Response("Cannot move goods to same storage", status=status.HTTP_400_BAD_REQUEST)
        
        if Goods.objects.get(id=goods_id) is None:
            return Response("Goods id missing or non existant", status=status.HTTP_400_BAD_REQUEST)
        storage_1 = Storage.objects.get(id=storage_1_id)
        storage_2 = Storage.objects.get(id=storage_2_id)
        if storage_1 is None or storage_2 is None:
            return Response("Could not find Storage models", status=status.HTTP_204_NO_CONTENT)
        goods_to_move = Storage_Goods.objects.get(storage_id=storage_1_id, goods_data_id=goods_id)
        if goods_to_move is None:
            return Response("No resources with that id available", status=status.HTTP_400_BAD_REQUEST)
        if goods_to_move.quantity < quantity:
            return Response("Not enough resources available", status=status.HTTP_400_BAD_REQUEST)
        move_to_goods = Storage_Goods.objects.get_or_create(storage_id=storage_2_id, goods_data_id=goods_id)
        if move_to_goods[1] and storage_2.number_of_storage_spaces <= Storage_Goods.objects.filter(storage_id=storage_2_id).count()+1:
            return Response("Not enough space in the second storage", status=status.HTTP_400_BAD_REQUEST)
        elif not move_to_goods[1] and move_to_goods[0].quantity + quantity > move_to_goods[0].max_stack_size:
            return Response("Storage space too small", status=status.HTTP_400_BAD_REQUEST)
        move_to_goods[0].quantity += quantity
        move_to_goods[0].save()
        goods_to_move.quantity -= quantity
        goods_to_move.save()
        return Response("Moved " +str(quantity) + " Goods:" + str(goods_id) + " from " + str(storage_1_id) + " to " + str(storage_2_id))
    
class SetCartInMotion(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CartSerializer
    
    def post(self, request):
        cartID = int(request.data["cartID"])
        if cartID is None:
            return Response("Please add the cart ID to the path params", status=status.HTTP_400_BAD_REQUEST)
        x = int(request.data["x"])
        y = int(request.data["y"])
        cart = Cart.objects.get(id=cartID)
        if cart.is_traveling:
            return Response("Cart already in motion", status=status.HTTP_400_BAD_REQUEST)
        if cart.current_x == x and cart.current_y == y:
            return Response("Cart already at location", status=status.HTTP_200_OK)
        grid = GridPoint.objects.filter(x=x,y=y,country=cart.character.country)
        if not grid:
            return Response("Grid point does not exist", status=status.HTTP_400_BAD_REQUEST)
        cart.UpdateCart()
        cart.target_x = x
        cart.target_y = y
        cart.travel_duration_seconds = abs(x - cart.current_x) + abs(y-cart.current_y) * cart.travel_speed_per_block
        cart.departure_time = datetime.now(UTC)
        cart.is_traveling = True
        cart.save()
        return Response("Cart in motion", status=status.HTTP_200_OK)