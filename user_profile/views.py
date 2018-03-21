from django.shortcuts import render, get_object_or_404, redirect
from .models import MyUser
from django.contrib.auth import login, logout


def registration(request):
    if request.method == 'POST':
        user = MyUser.objects.create_user(email=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect('/jobs/')
    else:
        return render(request, 'mail_sender/registration.html')


def log_in(request):
    if request.method == 'POST':
        user = get_object_or_404(MyUser, email=request.POST['username'])
        if user.check_password(raw_password=request.POST['password']):
            login(request, user)
            return redirect('/jobs/')
    else:
        return render(request, 'mail_sender/login.html')


def log_out(request):
    logout(request)
    return redirect('/user/login/')
  