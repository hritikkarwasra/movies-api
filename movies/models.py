from django.db import models
from datetime import date

# Create your models here.

class Genre(models.Model):
    id = models.AutoField(primary_key=True, null= False, blank= False)
    title = models.CharField(max_length=100, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Movie(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=255, blank= False)
    genre = models.ManyToManyField(Genre)
    director = models.CharField(max_length=100, null= True, blank= True)
    release_date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
