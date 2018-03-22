from django.shortcuts import render, get_object_or_404, redirect
from .models import MyUser
from .forms import ProfileForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm


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


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('/jobs/')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'mail_sender/edit_profile.html', {'form': form})
