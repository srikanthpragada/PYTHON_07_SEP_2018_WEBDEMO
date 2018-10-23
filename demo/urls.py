
from django.contrib import admin
from django.urls import path
from . import views, cookie_views

urlpatterns = [
    path("index/", views.index),
    path("about/", views.about),
    path("interest/", views.interest),
    path("movies/", cookie_views.list_movies),
    path("selectcity/", cookie_views.select_city),

]
