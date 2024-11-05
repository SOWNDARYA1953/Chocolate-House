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
