# inventory/models.py
from django.db import models

class SeasonalFlavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()  # Quantity in stock

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class CustomerSuggestion(models.Model):
    flavor_suggestion = models.CharField(max_length=100)
    allergy_concern = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.flavor_suggestion


class FlavorSuggestion(models.Model):
    flavor_name = models.CharField(max_length=100)
    allergy_concern = models.TextField(blank=True, null=True)
    # You can add a timestamp if you want to track when suggestions are added
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.flavor_name
