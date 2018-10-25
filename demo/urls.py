
from django.contrib import admin
from django.urls import path
from . import views, cookie_views, publisher_views

urlpatterns = [
    path("index/", views.index),
    path("about/", views.about),
    path("interest/", views.interest),
    path("movies/", cookie_views.list_movies),
    path("selectcity/", cookie_views.select_city),
    path("session_names/", cookie_views.session_names),
    path("person/", views.person_details),
    path("list_publishers/", publisher_views.list),
    path("add_publisher/", publisher_views.add),

]
