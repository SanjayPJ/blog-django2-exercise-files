from django.db import models

# Create your models here.

class Articles(models.Model):
     title = models.CharField(max_length=100)
     body = models.TextField()
     time = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title
     def snippet(self):
          return self.body[:350] + "..."