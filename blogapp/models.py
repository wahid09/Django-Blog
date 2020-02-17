from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.name.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Artical(models.Model):
     artical_author = models.ForeignKey(Author, on_delete=models.CASCADE)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     slug = models.SlugField()
     body = models.TextField()
     image = models.FileField()
     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
     active = models.BooleanField(default=True)

     def __str__(self):
         return self.title