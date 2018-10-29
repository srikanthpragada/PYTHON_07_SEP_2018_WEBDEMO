
from django.contrib import admin
from django.urls import path
from . import views, cookie_views, publisher_views, book_views

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
    path("delete_publisher/<int:pubid>", publisher_views.delete),
    path("list_books/", book_views.list),
    path("add_book/", book_views.add),
    path("delete_book/<int:bookid>", book_views.delete),
    path("edit_book/<int:bookid>", book_views.edit),
]
