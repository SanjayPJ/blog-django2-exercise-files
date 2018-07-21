from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Article(models.Model):
     
     title = models.CharField(max_length=100)
     body = models.TextField()
     slug = models.SlugField()
     date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title
     def snippet(self):
          return self.body[:350] + "..."