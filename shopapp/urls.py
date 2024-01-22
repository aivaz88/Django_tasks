from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('cube/', views.cube, name='cube'),
    path('random_number/', views.random_number, name='random_number'),
]