from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),

    path('travel_list', travel_list, name='travel_list'),
    path('travel_detail/<int:travel_id>/', travel_detail, name='travel_detail'),
    path('travel_create', travel_create, name='travel_create'),
]