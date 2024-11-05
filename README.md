# Chocolate-House
This is a chocolate house project

Project Structure and Steps

Set Up Django Project:
1.Start a new Django project and app:
           django-admin startproject chocolate_house
           cd chocolate_house
           python manage.py startapp inventory
2.Configure Database (SQLite):
    SQLite is Django's default database, so no configuration changes are needed in settings.py.
3.Define Models:
    Create models for Seasonal Flavors, Ingredients, and Customer Suggestions in inventory/models.py.
4.Create Admin Interface:
    Register models in inventory/admin.py for easy management in the Django admin panel.
5.Migrate the Database:
    Run migrations to create tables for your models.
          python manage.py makemigrations
          python manage.py migrate
6.Create Views and Templates:
    Create views for listing seasonal flavors, managing inventory, and handling customer suggestions in inventory/views.py.  
7.Create Forms for Customer Suggestions:
    In inventory/forms.py, create a form for handling customer flavor suggestions.    
8.Set Up URLs:
    Define URL patterns for each view in inventory/urls.py.
9.Integrate into Main Project URLs:
    Include the app URLs in chocolate_house/urls.py.   
10.Create Templates:
     Create templates (flavor_list.html, ingredient_list.html, and suggest_flavor.html) to display data and collect 
     suggestions. Place them in inventory/templates/inventory.
11. create superuser
     python manage.py createsuperuser
12.Run the project
     python manage.py runserver
