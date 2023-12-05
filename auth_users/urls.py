from django.urls import path
from . import views

urlpatterns = [
    path(route='registry/', view=views.registry, name='registry'),
    path(route='login/', view=views.user_login, name='login'),
]