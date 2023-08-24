
from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name= "home"),
    path('about',views.about, name= "about"),
    path("items/",views.startItems,name = "item_list"),
    path("items/<int:value>/",views.get_items,name = "item_detail")
]    + static(settings.STATIC_URL, documet_root=settings.STATIC_ROOT)


