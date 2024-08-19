from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from django.views.decorators.http import require_POST
from products.models import Products
from .forms import AddToCartForm
# Create your views here.
def cart_deatil_view(request):
    cart = Cart(request)


    for item in cart:
        item['product_update'] = AddToCartForm(initial={
            'quantity' : item['quantity'],
            'inplace' : True,
        })

    return render(request , 'cart/cart_detail.html',{
        'cart' : Cart(request),
    })



@require_POST
def add_to_cart_view(request,product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)
    form = AddToCartForm(request.POST) 
     

    if form.is_valid():
       cleaned_data = form.cleaned_data
       quantity = cleaned_data['quantity']
       cart.add(product,quantity,replace = cleaned_data['inplace'])

    return redirect('cart:cart_deatil',) 


def remove(request,product_id):

    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)

    cart.remove(product)
    
    return redirect('cart:cart_deatil') 
