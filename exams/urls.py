from django.urls import path
from . import views

urlpatterns = [
    path(route='request_exam/', view=views.request_exams, name='request_exams'),
]
