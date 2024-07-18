from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
