from django.contrib import admin
from .models import Exams, ExamsSolicitation, OrderExams

# Register your models here.
admin.site.register(Exams)
admin.site.register(ExamsSolicitation)
admin.site.register(OrderExams)
# TODO cadastrar items nas 3 tabelas através do menu admin na rota /admin