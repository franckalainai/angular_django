from enum import auto
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DecimalField

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=255, blank=True)

    price = DecimalField(default=0, max_digits=3, decimal_places=2)

    published = models.DateTimeField(blank=True, default=None, null=True)
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title