from django.shortcuts import render, get_object_or_404, redirect
from .models import MyUser
from .forms import ProfileForm, RegisterForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(raw_password=request.POST['password'])
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'],)
            login(request, new_user)
            return redirect('/jobs/')
    else:
        form = RegisterForm()
    return render(request, 'mail_sender/registration.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        user = get_object_or_404(MyUser, email=request.POST['username'])
        if user.check_password(raw_password=request.POST['password']):
            login(request, user)
            return redirect('/jobs/')
    else:
        return redirect("/")


def log_out(request):
    logout(request)
    return redirect('/')


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/jobs/')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'mail_sender/edit_profile.html', {'form': form})


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)

                return redirect('/user/me/')
        else:
            form = PasswordChangeForm(request.user)

        return render(request, 'mail_sender/change_password.html', {'form': form})
    return redirect('/login')

