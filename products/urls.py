from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductViews.as_view(), name='products'),
    path('<int:pk>/',views.ProducDetailView.as_view() ,name='product_detail')
]
