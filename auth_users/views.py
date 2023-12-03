from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def registry(request: json) -> HttpResponse:
    return HttpResponse('Hello world!')