from django.db import models

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
    exam_availability = models.BooleanField(default=False)
    exam_datetime = models.DateTimeField()

    def __str__(self):
        return self.exam_name