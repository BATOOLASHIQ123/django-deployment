from django.urls import path
from bat_app import views

urlpatterns =[
path('', views.index, name='index'),
]
