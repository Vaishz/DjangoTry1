from django.contrib import admin
from django.urls import path,include
from base import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('project', views.project, name= 'project'),
    path('reviews', views.reviews, name= 'reviews'),
    path('vaish', views.vaish, name= 'vaish'),
    path('kinda', views.kinda, name= 'kinda'),
]