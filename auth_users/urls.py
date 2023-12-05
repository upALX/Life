from django.urls import path
from . import views

urlpatterns = [
    path('registry/', views.registry, name='registry'),
    path('login/', views.login, name='login')
]