from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home'),
    path('callus/', views.AboutUsPageView.as_view(),name ='aboutus'),
]