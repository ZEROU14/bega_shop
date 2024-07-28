from django.urls import path
from . import views
from .views import test

urlpatterns = [
    path('',views.ProductViews.as_view(), name='products'),
    path('<int:pk>/',views.ProducDetailView.as_view() ,name='product_detail'),
    path('comment/<int:pk>/',views.CommentCreateView.as_view(), name = 'comments_creat'),
    path('hello/',test,)

]
