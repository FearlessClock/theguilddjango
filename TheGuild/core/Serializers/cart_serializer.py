from TheGuild.core.Models.CartModel import Cart
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'type', 'character', 'number_of_spaces', 'storage', 'location_type', 'location_id', 'target_location', 'travel_duration_seconds', 'departure_time']