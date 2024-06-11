from django.db import models
from musician.models import Musician
from django.forms import widgets

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    CHOICES = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
    }
    rating = models.CharField(max_length=10,choices=CHOICES)

    def __str__(self):
        return self.name