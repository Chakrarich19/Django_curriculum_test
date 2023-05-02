from django.urls import path
from .views import lecturers

urlpatterns = [
    path('lecturers', lecturers, name='lecturers'),
]