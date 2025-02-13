from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from TheGuild.core.Models.CharacterModel import Article, ShoppingCart
from django.core import serializers


# Python code​​​​​​‌​‌​‌‌‌‌‌​​​​​‌​‌​​​‌‌‌‌‌ below
def list_shopping_cart(request):
    user = request.user
    ShoppingCart.objects.get(user=user)
    serialized_data = serializers.serialize("json", ShoppingCart.objects.get(user=user))
    return JsonResponse(serialized_data)


def add_article_to_cart(request):
    pass


def add_articles_to_cart(request):
    pass
