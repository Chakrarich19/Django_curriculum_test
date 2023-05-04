from django.urls import path
from .views import Homepage, About, Curriculum_add

urlpatterns = [
    path('', Homepage, name='homepage'),
    path('about', About, name='about'),
    path('curriculumadd', Curriculum_add, name='curriculum_add'),
]