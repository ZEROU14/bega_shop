from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.
from .models import Blogs
from django.utils.translation import gettext as _



class BlogListView(generic.ListView):
    # model = Blogs
    queryset = Blogs.objects.filter(active = True)
    context_object_name = 'blogs'
    template_name = 'blogs/blog_list.html'


class BlogDetailView(generic.DetailView):
    model = Blogs
    context_object_name = 'blogs'
    template_name = 'blogs/blog_detail.html'