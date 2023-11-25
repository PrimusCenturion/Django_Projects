from .models import Book
from django import forms

class BookForm(forms.ModelForm):
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['publication_date'].widget.input_type = 'date'
    #     self.fields['publication_date'].widget.attrs['class'] = 'form-control'
            

    class Meta:
        model = Book
        fields = [
            "title", 
            "author", 
            "publication_date", 
            "genre", 
            "summary", 
            "isbn", 
            "number_of_pages",
            "language", 
            "keywords", 
        ]

        widgets = dict(
            publication_date = forms.TextInput(attrs={'type':'date'})
            )