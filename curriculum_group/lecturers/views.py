from django.shortcuts import render

def lecturers(request):
    return render(request, 'lecturers/lecturers.html')