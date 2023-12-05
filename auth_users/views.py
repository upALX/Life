from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login
import traceback
from time import sleep

# Create your views here.
def registry(request):
    if request.method == 'GET':
        return render(request, 'registry.html')
    elif request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name') 
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
                messages.add_message(request, constants.SUCCESS, f'Information of {user.username} saved with success!!!')
                sleep(2)
            except Exception as ex:
                messages.add_message(request, constants.ERROR, 'Internal error of system...')
                print('DEBUG', traceback.format_exc())
                return redirect('/users/registry/') 
            
            return redirect('/users/login')

def user_login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_auth = authenticate(username=username, password=password)
        print(user_auth)
        if user_auth:
            login(request=request, user=user_auth)
            return redirect('/platform')
        else:
            messages.add_message(
                request=request, 
                level=constants.ERROR, 
                message='Username or password invalid. Verify if you was create an account before try to login.')
            return redirect('/users/login/')
