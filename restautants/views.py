from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny,IsAuthenticated)
from .models import (Restaurant,MenuItem,RestaurantLike,MenuItemLike,SavedMenuItem)
from .serializers import (RestaurantSerializer)




class RestaurantListView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        restaurants = Restaurant.objects.all()

        serializer = RestaurantSerializer(
            restaurants,
            many=True
        )

        return Response(serializer.data)
    
class RestaurantLikeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        try:
            restaurant = Restaurant.objects.get(
                id=pk
            )
        except Restaurant.DoesNotExist:
            return Response(
                {"error": "Restaurant not found"},
                status=404
            )

        like, created = RestaurantLike.objects.get_or_create(
            user=request.user,
            restaurant=restaurant
        )

        if not created:
            return Response(
                {
                    "message":
                    "Already liked"
                }
            )

        return Response(
            {
                "message":
                "Restaurant liked successfully"
            }
        )    
        
class MenuItemLikeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        try:
            menu_item = MenuItem.objects.get(
                id=pk
            )

        except MenuItem.DoesNotExist:

            return Response(
                {
                    "error":
                    "Menu item not found"
                },
                status=404
            )

        like, created = MenuItemLike.objects.get_or_create(
            user=request.user,
            menu_item=menu_item
        )

        if not created:

            return Response(
                {
                    "message":
                    "Already liked"
                }
            )

        return Response(
            {
                "message":
                "Menu item liked successfully"
            }
        )        
        
        
class SaveMenuItemView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        try:
            menu_item = MenuItem.objects.get(
                id=pk
            )

        except MenuItem.DoesNotExist:

            return Response(
                {
                    "error":
                    "Menu item not found"
                },
                status=404
            )

        saved, created = SavedMenuItem.objects.get_or_create(
            user=request.user,
            menu_item=menu_item
        )

        if not created:

            return Response(
                {
                    "message":
                    "Already saved"
                }
            )

        return Response(
            {
                "message":
                "Menu item saved successfully"
            }
        )        