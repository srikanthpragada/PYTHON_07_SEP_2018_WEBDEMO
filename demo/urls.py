
from django.contrib import admin
from django.urls import path
from . import views, cookie_views, publisher_views, book_views, ajax_views, class_views

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
    path("list_books/", book_views.list_books),
    path("add_book/", book_views.add_book),
    path("delete_book/<int:bookid>", book_views.delete_book),
    path("edit_book/<int:bookid>", book_views.edit_book),
    path("search_form", book_views.search_form),
    path("search_books", book_views.search_books),
    path("ajax_demo", ajax_views.demo),
    path("ajax_now", ajax_views.now),
    path("ajax_avg_price", ajax_views.average_price),
    path("aboutus", class_views.AboutView.as_view()),
    path("books", class_views.ListBooks.as_view()),

]
