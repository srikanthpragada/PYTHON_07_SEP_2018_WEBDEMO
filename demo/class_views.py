from django.views.generic import TemplateView, ListView
from . models import Book

class AboutView(TemplateView):
    template_name = "aboutus.html"


class ListBooks(ListView):
    context_object_name = 'books'
    model = Book