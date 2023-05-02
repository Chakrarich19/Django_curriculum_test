from django.shortcuts import render
from .models import Faculty, Curriculum

def Homepage(request):
    all_program = Curriculum.objects.all()
    context = {'all_program': all_program}
    return render(request, 'curriculums/homepage.html', context)

def About(request):
    return render(request, 'curriculums/about.html')


