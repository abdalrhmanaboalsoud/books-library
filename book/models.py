from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    """
    Model for representing a book in the library database.
    """
    # ForeignKey to the User model provided by Django's authentication system.
    # When a user is deleted, all their books are deleted as well.
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # The title of the book.
    title = models.CharField(max_length=100, blank=False, null=False)
    # A description of the book.
    description = models.TextField()
    # A numerical rating of the book's quality.
    rating = models.IntegerField()
    # The date the book was published.
    publish_date = models.DateField()
    

    def __str__(self):
        return f'{self.title} by {self.author} (Description: {self.description}) (Rating: {self.rating}) (Publish Date: {self.publish_date})'



    
