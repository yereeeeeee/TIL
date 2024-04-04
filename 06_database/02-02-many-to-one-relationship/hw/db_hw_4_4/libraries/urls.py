from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    path('<int:pk>/review_create/', views.review_create, name='review_create'),
    path('<int:book_pk>/reviews/<int:review_pk>/delete/', views.reviews_delete, name='reviews_delete'),
]
