from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def registry(request):
    if request.method == 'GET':
        return render(request, 'registry.html')
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name') 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password: str = request.POST.get('password')
        confirmation_password = request.POST.get('c-password')

        if not password == confirmation_password:
            messages.add_message(request, constants.ERROR, 'The password and the confirmation need be equals.')
            return redirect('/users/registry/')
        elif len(password) < 8:
            messages.add_message(request, constants.ERROR, 'Your password chosen must be greater than 7')
            return redirect('/users/registry/') 
        #TODO validate if the username of user NOT exists on database, because the database return an error when try input a username that already exist on DB
        else:
            try:
                user = User.objects.create_user(
                    first_name=first_name, 
                    last_name=last_name, 
                    username=username, 
                    email=email, 
                    password=password
                )
                messages.add_message(request, constants.SUCCESS, 'Information saved with success!!!')
            except:
                messages.add_message(request, constants.ERROR, 'Internal error of system...')
                return redirect('/users/registry/') 

            