from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:todo_pk>/', views.detail, name='detail'),
    # path('new_todo/', views.new_todo, name='new_todo'),
    path('<int:todo_pk>/delete/', views.delete, name='delete'),
    path('<int:todo_pk>/update/', views.update, name='update'),
    # path('<int:todo_pk>/edit_todo/', views.edit_todo, name='edit_todo'),
]