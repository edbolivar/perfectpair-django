from django.urls import path
from . import views


app_name = 'customerservice'

urlpatterns = [
    path('', views.show, name='show'),
    path('pricing', views.pricing, name='pricing'),
    path('faq', views.faq, name='faq'),

]




