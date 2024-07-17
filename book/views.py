from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class BookView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'book.html'
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'books_details.html'
