from django.shortcuts import render
from django.views import generic

from .models import Products

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