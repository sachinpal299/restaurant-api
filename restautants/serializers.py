from rest_framework import serializers
from .models import (Restaurant,MenuItem,RestaurantLike,MenuItemLike,SavedMenuItem)

class MenuItemSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "description",
            "price",
            "like_count"
        ]

    def get_like_count(self, obj):
        return obj.likes.count()
    
    
class RestaurantSerializer(serializers.ModelSerializer):

    menu_items = MenuItemSerializer(
        many=True,
        read_only=True
    )

    restaurant_like_count = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "address",
            "description",
            "restaurant_like_count",
            "menu_items"
        ]

    def get_restaurant_like_count(self, obj):
        return obj.likes.count()    
    
    
class RestaurantLikeSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = RestaurantLike
        fields = "__all__"    
        
class MenuItemLikeSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = MenuItemLike
        fields = "__all__"        
        
class SavedMenuSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = SavedMenuItem
        fields = "__all__"        