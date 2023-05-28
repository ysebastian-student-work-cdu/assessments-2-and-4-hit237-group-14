from django.contrib import admin
from django.urls import path, include, re_path
from admin_g14 import views

# app_name = 'notices'

urlpatterns = [
    path('',views.model_list,name='admin-home'),
    path('<str:model>/create', views.create, name='create'),
    path('<str:model>/view', views.view, name='view'),
    path('<str:model>/delete', views.delete, name='delete'),
    path('<str:model>/<int:pk>/edit', views.edit, name='edit'),
    path('<str:model>/<int:pk>/save', views.save, name='save'),
]