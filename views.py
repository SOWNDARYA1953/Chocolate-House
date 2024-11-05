# inventory/views.py
from django.shortcuts import render, redirect
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion
from .forms import SuggestionForm
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import FlavorSuggestion


def homepage(request):
    featured_flavors = FlavorSuggestion.objects.all()  # Retrieves all flavors
    return render(request, 'inventory/homepage.html', {'featured_flavors': featured_flavors})
#def homepage(request):
    #return render(request, 'inventory/homepage.html')



def flavor_list(request):
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'inventory/flavor_list.html', {'flavors': flavors})

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

def suggest_flavor(request):
    submitted = False  # Default value to indicate submission status
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the suggestion
            submitted = True  # Set to True if form is submitted successfully
    else:
        form = SuggestionForm()  # If GET request, instantiate an empty form

    return render(request, 'inventory/suggest_flavor.html', {'form': form, 'submitted': submitted})

from django.urls import reverse  # for named URL patterns

def suggest_flavor(request):
    if request.method == 'POST':
        # Process the form data here
        # e.g., save flavor suggestion

        # After form submission, redirect to thank_you page
        return redirect('thank_you')  # Use the name of the thank you URL pattern

    return render(request, 'inventory/suggest_flavor.html')
    

class ThankYouView(TemplateView):
    template_name = 'inventory/thank_you.html'  # Ensure this points to your thank-you template

def thank_you(request):
    return render(request, 'inventory/thank_you.html')    