from django.db import models

from django.shortcuts import reverse
from django.contrib.auth import get_user_model
# Create your models here.




class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    
class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager,self).get_queryset().filter(active = True)






class Comments(models.Model):
    PRODUCT_STARS = [
        ('1', 'very bad'),
        ('2','bad'),
        ('3','noraml'),
        ('4','good'),
        ('5','very good'),
        
    ]
    product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='comments')
    stars = models.CharField(max_length=10 ,choices=PRODUCT_STARS )
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Manager

    objects = models.Manager()
    
    active_comment_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
    