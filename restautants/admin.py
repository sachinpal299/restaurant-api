from django.contrib import admin
from .models import (
    Restaurant,
    MenuItem,
    RestaurantLike,
    MenuItemLike,
    SavedMenuItem
)

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(RestaurantLike)
admin.site.register(MenuItemLike)
admin.site.register(SavedMenuItem)