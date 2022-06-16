from tkinter import CASCADE
from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Article(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField('Category')
    desc = models.TextField()

    def __str__(self):
        return f'{self.title} ({self.author})'
