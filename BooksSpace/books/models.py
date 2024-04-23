from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='books/%Y/%m/%d')

    def __str__(self):
        return self.name
    

class author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class publishing(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class book(models.Model):
    image = models.ImageField(upload_to='books/%Y/%m/%d')
    name_book = models.CharField(max_length=255)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publishing = models.ForeignKey(publishing, on_delete=models.CASCADE)
    series = models.CharField(max_length=255)
    year_publishing = models.IntegerField()
    file_book = models.FileField(upload_to='file_books/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name_book
    
    
class in_planes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_books = models.ForeignKey(book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Favorites"
   