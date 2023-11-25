from django.views.generic.edit import CreateView
from django import forms

from .models import Book
from .forms import BookForm

class BookCreateView(CreateView):

        model = Book
        form_class = BookForm
        template_name = 'index.html'
        # fields = [
        #     "title", 
        #     "author", 
        #     "publication_date", 
        #     "genre", 
        #     "summary", 
        #     "isbn", 
        #     "number_of_pages",
        #     "language", 
        #     "keywords", 
        # ]


