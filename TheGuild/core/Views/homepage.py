from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from TheGuild.core.Models.CountryModel import Country
from TheGuild.core.Models.CharacterModel import Character
from rest_framework.authtoken.models import Token

def Homepage(request):
    assert isinstance(request, HttpRequest)
    data = {'token': Token.objects.get(user=request.user),
            'countries': Country.objects.all()}
    countryId = request.GET.get('country', -1)
    if countryId != -1: 
        data['characters'] = Character.objects.filter(country_id=countryId, user=request.user)
    return render(
        request,
        'core/index.html',
        data
    )