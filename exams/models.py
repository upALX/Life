from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exams(models.Model):
    type_choices = (
        ('H', 'Hemograma exam'),
        ('C', 'Colesterol'),
        ('G', 'Glicose'),
        ('I', 'Ionograma'),
        ('X', 'Raio-X'),

    )
    exam_name = models.CharField(max_length=50)
    exam_type = models.CharField(max_length=1, choices=type_choices)
    exam_price = models.FloatField()
    exam_availability = models.BooleanField(default=True)
    

    def __str__(self):
        return self.exam_name
    
class ExamsSolicitation(models.Model):
    choice_status = (
        ('A', 'Under analysis'),
        ('F', 'Finished')
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exam = models.ForeignKey(Exams, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=choice_status)
    result = models.FileField(upload_to='exams_result', null=True, blank=True)
    password_required = models.BooleanField(default=False)
    password = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f'{self.user} | {self.exam.name}'

class OrderExams(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exams = models.ManyToManyField(ExamsSolicitation)
    is_scheduled = models.BooleanField(default=True)
    date = models.DateField()

    def __str__(self) -> str:
        return f'{self.user} | {self.date}'
