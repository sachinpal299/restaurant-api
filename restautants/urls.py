from django.urls import path
from .views import (RestaurantListView,RestaurantLikeView,MenuItemLikeView,SaveMenuItemView)

urlpatterns = [
    path("restaurants/",RestaurantListView.as_view()),
    path("restaurants/<int:pk>/like/",RestaurantLikeView.as_view()),
    path("menu-items/<int:pk>/like/",MenuItemLikeView.as_view()),
    path("menu-items/<int:pk>/save/",SaveMenuItemView.as_view()),
]


