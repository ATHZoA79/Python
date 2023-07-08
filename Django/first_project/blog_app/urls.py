# Route Setting Here

from django.urls import path
from . import views # import views from project folder

urlpatterns = [
    path('', views.home, name='blog-index'),
    path('about/', views.about, name='blog-about')
]