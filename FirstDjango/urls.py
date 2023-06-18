
from django.contrib import admin
from django.urls import path
from MainApp import views
urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path("items/",views.startItems),
    path("items/<int:value>/",views.get_items)
]

