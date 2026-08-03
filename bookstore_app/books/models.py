from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    thumbnail = models.URLField(null=True)
    pageCount = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    body = models.TextField()