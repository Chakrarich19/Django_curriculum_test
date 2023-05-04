from django.shortcuts import render
from .models import Faculty, Curriculum

def Homepage(request):
    all_program = Curriculum.objects.all()
    context = {'all_program': all_program}
    return render(request, 'curriculums/homepage.html', context)

def About(request):
    return render(request, 'curriculums/about.html')

def Curriculum_add(request):
    all_faculty = Faculty.objects.all()
    context = {'all_faculty': all_faculty}

    if request.method == 'POST':
        data = request.POST.copy()
        print('DATA', data)
        code = data.get('code')
        name = data.get('name')
        program = data.get('program')
        degree = data.get('degree')
        faculty_id = data.get('faculty')
        approve_at = data.get('approve_at')

        faculty = Faculty.objects.get(id=faculty_id)

        newcurriculum = Curriculum()
        newcurriculum.code = code
        newcurriculum.name = name
        newcurriculum.program = program
        newcurriculum.degree = degree
        newcurriculum.faculty = faculty
        newcurriculum.approve_at = approve_at
        newcurriculum.save()

    return render(request, 'curriculums/curriculum_add.html', context)




