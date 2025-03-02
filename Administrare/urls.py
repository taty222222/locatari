"""
URL configuration for Administrare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from locatari import views
from locatari.views import home, HomeView, about, plata_card, lista_facturi, submit_reclamatii, \
    add_water_meter_reading

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('locatari.urls')),
    path('home/', HomeView.as_view(template_name='locatari/home.html'), name='home'),  # Updated line
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='locatari/login.html'), name='login'),

    path('about/', about, name='about'),
    path('submit_reclamatii/', submit_reclamatii, name='submit_reclamatii'),
    path('add_water_meter_reading/', add_water_meter_reading, name='add_water_meter_reading'),

    path('istoric_facturi/', lista_facturi, name='istoric_facturi'),
    path('locatari/', views.list_locatari, name='locatari'),
    path('plata_card/', plata_card,name='plata_card'),
     path('list_water_meter_reading/', views.list_water_meter_reading, name='list_water_meter_reading'),


    path('avize/', views.lista_aviz, name='lista_avize'),
    path('avize/adauga/', views.generate_aviz, name='adauga_aviz'),
    path('istoric_plati/', views.istoric_plati, name='istoric_plati'),

]
