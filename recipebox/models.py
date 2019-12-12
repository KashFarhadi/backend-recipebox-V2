"""
Author
    Name
    Bio

Recipe
    Author
    Title
    Description
    Time Required
    Instructions 

"""
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
