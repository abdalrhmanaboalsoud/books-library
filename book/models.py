from django.db import models
from django.contrib.auth import get_user_model

class Book(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=False, null=False, primary_key=False)
    description = models.TextField(max_length=200, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title