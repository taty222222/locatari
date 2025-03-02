from django.urls import path

from . import views
from .views import (
    home, signup, lista_apartamente, lista_facturi, submit_reclamatii,
    reclamatii_list, sterge_factura, sterge_apartament, about,
    plata_card, logout_view, adauga_factura, generate_aviz,
    istoric_plati, add_water_meter_reading
)
from django.contrib.auth import views as auth_views
from .forms import LoginForm


LOGIN_TEMPLATE = 'locatari/login.html'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name=LOGIN_TEMPLATE, authentication_form=LoginForm),
         name='login'),
    path('logout/', logout_view, name='logout'),
    path('apartamente/', lista_apartamente, name='lista_apartamente'),
    path('lista-facturi/', lista_facturi, name='lista_facturi'),
    path('submit-reclamatii/', submit_reclamatii, name='submit_reclamatii'),
    path('reclamatii-list/', reclamatii_list, name='reclamatii_list'),
    path('facturi/sterge/<int:pk>/', sterge_factura, name='sterge_factura'),
    path('locatari_locator/', views.list_locatari, name='locatari_locatar'),
    path('apartament/sterge/<int:pk>/', sterge_apartament, name='sterge_apartament'),
    path('istoric-plati/', istoric_plati, name='istoric_plati'),
    path('about/', about, name='about'),
    path('add_water_meter_reading/', add_water_meter_reading, name='add_water_meter_reading'),
    path('list_water_meter_readings/', views.list_water_meter_reading, name='list_water_meter_readings'),
    path('plata-card/', plata_card, name='plata_card'),
    path('avize/adauga/', generate_aviz, name='generate_aviz'),
    path('adauga-factura/', adauga_factura, name='adauga_factura'),
]
