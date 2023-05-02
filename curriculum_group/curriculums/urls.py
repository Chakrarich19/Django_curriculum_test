from django.urls import path
from .views import Homepage, About

urlpatterns = [
    path('', Homepage, name='homepage'),
    path('about', About, name='about'),
]