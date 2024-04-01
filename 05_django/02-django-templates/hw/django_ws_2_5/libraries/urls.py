from django.contrib import admin
from django.urls import path, include
from libraries import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.recommend, name='recommend'),
    path('bestseller/', views.bestseller, name='bestseller'),
]
