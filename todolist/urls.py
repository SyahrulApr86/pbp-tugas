from django.urls import path
from todolist.views import *


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('set-task/<int:pk>', ubah_status, name='ubah_status'),
    path('delete/<int:pk>', hapus, name='hapus'),
    path('add/', todolist_ajax, name="todolist_ajax" ),
    path('json/', show_json, name="show_json"),
]