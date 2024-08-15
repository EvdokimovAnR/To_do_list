from django.urls import path
from .views import index, add, delete, completed,  edit_todo

app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('completed/<int:todo_id>/', completed, name='completed'),
    path('edit_todo/<int:todo_id>/', edit_todo, name='edit_todo')
]