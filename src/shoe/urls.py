from django.urls import path
from . import views


app_name = 'shoe'

urlpatterns = [
    path('', views.shoe_list, name='shoe_list'),
    path('liked_list', views.liked_list, name="liked_list"),
    path('cart_list/<shoe_id>', views.cart_list, name="cart_list"),
   	path('gender_male', views.gender_male, name="gender_male"),
   	path('gender_female', views.gender_female, name="gender_female"),
   	path('s', views.search, name="search"),
   	path('sidebar', views.sidebar, name="sidebar"),
   	path('men_sneakers', views.men_sneakers, name="men_sneakers"),
   	path('men_business', views.men_business, name="men_business"),
   	path('men_casual', views.men_casual, name="men_casual"),
   	path('men_boots', views.men_boots, name="men_boots"),
   	path('men_sandals', views.men_sandals, name="men_sandals"),
   	path('women_sneakers', views.women_sneakers, name="women_sneakers"),
   	path('women_flats', views.women_flats, name="women_flats"),
   	path('women_pumps', views.women_pumps, name="women_pumps"),
   	path('women_boots', views.women_boots, name="women_boots"),
   	path('women_sandals', views.women_sandals, name="women_sandals"),
	path('new_arrivals', views.new_arrivals, name="new_arrivals"),
	path('like', views.like, name="like"),

]

