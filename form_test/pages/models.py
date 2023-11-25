from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    genre = models.CharField(max_length=200)
    summary = models.TextField()
    isbn = models.BigIntegerField()
    number_of_pages = models.BigIntegerField()
    language = models.CharField(max_length=200)
    keywords = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_create')