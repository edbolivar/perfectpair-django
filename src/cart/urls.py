from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.view, name='shoe_list'),
 
 
]