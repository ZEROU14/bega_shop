from django.urls import path

from .views import cart_deatil_view,add_to_cart_view,remove

app_name = 'cart'

urlpatterns = [
    path('',cart_deatil_view, name = 'cart_deatil'),
    path('add/<int:product_id>/',  add_to_cart_view , name='add_to_cart'),
    path('remove/<int:product_id>/',  remove , name='remove')

]
