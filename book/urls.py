from django.urls import path
from .views import HomeView, BookView, BookDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/', BookView.as_view(), name='book'),
    path('<int:pk>/', BookDetailView.as_view(), name='books_details'),  # Add the 'book/' prefix here
]
