from django.db import models

class Faculty(models.Model):
    Faculty_type= (
        ('วิทยาศาสตร์และเทคโนโลยี','วิทยาศาสตร์และเทคโนโลยี'),
        ('มนุษยศาสตร์และสังคมศาสตร์','มนุษยศาสตร์และสังคมศาสตร์')
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=Faculty_type)

    def __str__(self):
        return self.name
    
class Curriculum(models.Model):
    curriculum_degree= (
        ('ปริญญาตรี','ปริญญาตรี'),
        ('ปริญญาโท','ปริญญาโท'),
        ('ปริญญาเอก','ปริญญาเอก')
    )

    code = models.CharField(max_length=9)
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    degree = models.CharField(max_length=40, choices=curriculum_degree,default='ปริญญาตรี')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    approve_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
