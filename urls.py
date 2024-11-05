# inventory/urls.py
from django.urls import path
from . import views 
from .views import ThankYouView
urlpatterns = [
    path('flavors/', views.flavor_list, name='flavor_list'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('suggest/', views.suggest_flavor, name='suggest_flavor'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'),
]


# chocolate_house/urls.py
from django.contrib import admin
from django.urls import path, include
from inventory import views as inventory_views  # Import the homepage view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),  # Existing routes for inventory app
    path('', inventory_views.homepage, name='homepage'),  # Homepage route
   
]
