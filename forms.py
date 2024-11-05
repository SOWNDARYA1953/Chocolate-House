# inventory/forms.py
from django import forms
from .models import CustomerSuggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['flavor_suggestion', 'allergy_concern']

        
