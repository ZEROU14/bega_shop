from django.contrib import admin

from .models import Products

# admin.site.register(Products)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']
    

# Register your models here.