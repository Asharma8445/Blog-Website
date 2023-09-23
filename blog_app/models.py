from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        url = ""
        try:
            url = self.image.url 
        except: 
            url = ""
        return url

    
class Author(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=65)
    image = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + " | " + self.email
    
    @property
    def imageURL(self):
        url = ""
        try:
            url = self.image.url 
        except: 
            url = ""
        return url

class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_now=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title + " | " + self.category.name
    
    @property
    def imageURL(self):
        url = ""
        try:
            url = self.image.url 
        except: 
            url = ""
        return url
    

class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=40)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)


    
# User Authorization & User Authentication