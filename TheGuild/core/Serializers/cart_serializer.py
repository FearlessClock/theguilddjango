from TheGuild.core.Models.CartModel import Cart
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'type', 'character', 'storage', 'location_type', 'location_id', 'current_x', 'current_y', 'target_x', 'target_y', 'travel_duration_seconds', 'departure_time', 'is_traveling']