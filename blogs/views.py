from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Blogs


class BlogListView(generic.ListView):
    # model = Blogs
    queryset = Blogs.objects.filter(active = True)
    context_object_name = 'blogs'
    template_name = 'blogs/blog_list.html'