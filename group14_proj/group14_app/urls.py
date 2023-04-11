from django.contrib import admin
from django.urls import path, re_path

from group14_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='homepage'),
    path('home/', views.home, name ='homepage'),
    path('list/', views.list, name ='list'),
    path('details/<int:id>/', views.details, name = 'details'),
    re_path(r'^details/(?P<id>[1-6]{1})/?$', views.details),
    path('data_model/', views.data_model, name ='data_model'),
]
