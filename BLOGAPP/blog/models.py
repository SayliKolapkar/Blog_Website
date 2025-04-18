from django.db import models
from django.contrib.auth.models import User

#Create a Category model for categorizing posts
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Define models for Post (title, content, category, published_date, author)   
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(auto_now_add =True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title

