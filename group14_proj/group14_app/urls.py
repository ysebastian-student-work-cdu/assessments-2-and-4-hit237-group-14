from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='homepage'),
    path('list/', views.list, name ='list'),
    path('details/', views.details, name ='details'),
    path('data_model/', views.data_model, name ='data_model'),

    #path('now/',views.now, name="now"),
]
