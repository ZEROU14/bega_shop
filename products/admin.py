from django.contrib import admin

from .models import Products , Comments


# admin.site.register(Products)




@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']
    

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body','stars']

