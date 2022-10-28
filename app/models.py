from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=50)

class Album(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    year_of_release = models.DateField(default=timezone.now)

class Song(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Author, on_delete=models.CASCADE)