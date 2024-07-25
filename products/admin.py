from django.contrib import admin

from .models import Products , Comments


# admin.site.register(Products)

class ProductCommentsInLine(admin.StackedInline):
    model = Comments
    fields = ['body','stars','author']
    extra = 0

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']
    
    inlines =[
        ProductCommentsInLine
    ]

# @admin.register(Comments)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['body','stars']

