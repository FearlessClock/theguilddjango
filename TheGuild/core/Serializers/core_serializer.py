from django.contrib.auth.models import Group, User
from rest_framework import serializers
from ..Models.CountryModel import Country
from ..Models.CharacterModel import Character

class CountrySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'tick', 'last_update','country_start_date', 'tick_in_seconds']
        
        
class CharacterSerialzer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Character
        fields = ['id', 'country', 'user', 'name']