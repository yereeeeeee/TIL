from django.urls import path
from . import views
from .models import Restaurant

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
