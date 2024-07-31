from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100,verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    
    active = models.BooleanField(default=True,verbose_name=_('active'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blogdetail", args=[self.pk])