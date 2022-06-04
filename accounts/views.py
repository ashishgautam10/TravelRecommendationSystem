from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from .models import *
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if UserProfile.objects.filter(username=username).exists():
                E_message = "username already taken"
                messages.add_message(request, 951, E_message)
                print('username taken')
                return render(request, 'travelapp/register.html')
            elif UserProfile.objects.filter(email=email).exists():
                msg = "email already taken"
                messages.add_message(request, 951, msg)
                print('email taken')
                return render(request, 'travelapp/register.html')
            else:
                user = UserProfile.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password1,
                    email=email
                )
                user.save()
                messg = "registered successfully"
                messages.add_message(request, 159, messg)
                user = auth.authenticate(username=username, password=password1)
                print('user created')
                return redirect("/")
        else:
            message = "Password are not same"
            messages.add_message(request, 951, message)
            print("password doesn't match")
            return render(request, 'travelapp/register.html')
    else:
        return render(request, 'travelapp/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:    
            auth.login(request, user)
            messg = "logged in"
            messages.add_message(request, 159, messg)
            print("logged in")
            return redirect("/")
        else:
            msg = "invalid credential"
            messages.add_message(request, 159, msg)
            return redirect('login')
    else:
        return render(request, 'travelapp/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
