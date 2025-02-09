from django.shortcuts import render
from rest_framework import generics, permissions, status
from ..Models.MarketplaceModel import Stall
from ..Models.CartModel import Cart
from ..Models.GoodsModel import ItemInformation
from ..Models.StorageModel import Storage_Goods, Storage
from ..Models.CharacterModel import Character
from rest_framework.views import APIView
from ..Serializers.marketplace_serializer import StallSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse

class StallListAllView(generics.ListCreateAPIView):
    queryset = Stall.objects.all()
    serializer_class = StallSerializer
    
class StallListByCountryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StallSerializer
    
    def get_queryset(self):
        filter = self.kwargs['countryID']
        if filter is not None:
            queryset = Stall.objects.filter(country_id=filter)
            return queryset
        return None
    
class StallDetailView(generics.RetrieveUpdateAPIView):
    queryset = Stall.objects.all()
    serializer_class = StallSerializer
    permission_classes = [IsAuthenticated]
    
class SellToStall(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        cartID = request.data["cartID"]
        stallID = request.data["stallID"]
        goodsID = request.data["goodsID"]
        quantity = request.data["quantity"]
        try:
            cart = Cart.objects.get(id=cartID)
        except ObjectDoesNotExist:
            return Response("Cart not found", status=status.HTTP_400_BAD_REQUEST)
        
        try:
            stall = Stall.objects.get(id=stallID)
        except ObjectDoesNotExist:
            return Response("Stall not found", status=status.HTTP_400_BAD_REQUEST)
        
        if cart.location_id != stall.building.id or cart.location_type!=stall.building.type:
            return Response("Cart not at stall", status=status.HTTP_400_BAD_REQUEST)
        
        try:
            goods = Storage_Goods.objects.get(storage_id=stall.storage.id, goods_data_id=goodsID)
        except:
            return Response({'message':"Stall doesn't contain this goods"})
        
        try:
            cart_goods = Storage_Goods.objects.get(goods_data_id=goodsID, storage_id=cart.storage.id)
        except ObjectDoesNotExist:
            return Response("Goods not in Cart", status=status.HTTP_400_BAD_REQUEST)

        if cart_goods.quantity < quantity:
            if cart_goods.quantity == 0:
                cart_goods.delete()
            return Response("Not enough goods to sell", status=status.HTTP_400_BAD_REQUEST)
        
        character = cart.character
        goods = ItemInformation.objects.get(id=goodsID)
        price = goods.GetCurrentPrice()
        cart_goods.quantity = cart_goods.quantity - quantity
        character.money += price * quantity
        if cart_goods.quantity == 0:
            cart_goods.delete()
        else:
            cart_goods.save()
        character.save()
        return Response("Sold "+ str(quantity) + " " + goods.name + " to "+ stall.building.name + " for " + str(price) + " " + character.name + " now has " + str(character.money) + " money", status=status.HTTP_200_OK )
        
        
        
        
