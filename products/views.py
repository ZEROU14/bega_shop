from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404 ,reverse
from django.views import generic

from .forms import CommentForm
from .models import Products,Comments
from django.utils.translation import gettext as _
from django.contrib import messages
from cart.forms import AddToCartForm
# Create your views here.



class ProductViews(generic.ListView):
    # model = Products
    queryset = Products.objects.filter(active = True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProducDetailView(generic.DetailView):
    model = Products
    template_name = 'products/product_detail_view.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart'] = AddToCartForm()

        return context
    
class CommentCreateView(generic.CreateView):
    model = Comments
    form_class = CommentForm
    
  

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Products, id = product_id)

        obj.product = product

        messages.success(self.request,'your comment is down there and you can see it dude')

        return super().form_valid(form)
