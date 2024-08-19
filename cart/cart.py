from django.contrib import messages
from products.models import Products



class Cart:
    def __init__(self,request):

        """
        init the cart
        
        """

        # here we take the request from user
        self.request = request
 
        # and here we get the session  of that user
        self.session = request.session

        #here we are gonna search that if there is a cart object in the session or not
        cart = self.session.get('cart')

        # and in this part we say if the cart is not craeted befor creat one for us
        if not cart: 
           cart = self.session['cart'] = {}
            # cart = self.session['cart'] = {}

        # and then we save it
        self.cart = cart

        # here we add the id of product and the number of that product ,DEFAUTL IS = 1
    def add(self,product,quantity=1, replace = False):
        """
        and in this part we creat the function for add things to our cart
        """
        product_id = str(product.id) 
        
        # 
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0}

        if replace:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        messages.success(self.request,'Product added to your Cart Successfuly')

        self.save()

    def remove(self,product):
        """remove product from user cart"""

        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            messages.success(self.request,('Product removed from your cart'))


            
    def save(self):
        self.session.modified = True



    def __iter__(self):
       product_ids = self.cart.keys()
       products = Products.objects.filter(id__in = product_ids)

       cart = self.cart.copy()


       for product in products:
           cart[str(product.id)]['product_obj'] = product

       for item in cart.values():
           item['total_price'] = item['product_obj'].price * item['quantity']
           yield item

    def __len__(self):
        return len(self.cart.keys())
    

    def clear(self):
        del self.session['cart']
        self.save()


    def get_total_price(self):
       product_ids = self.cart.keys()
    #    products = Products.objects.filter(id__in=product_ids)

       return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())