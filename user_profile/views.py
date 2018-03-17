from django.shortcuts import get_object_or_404, render


def registration(request):
    return render(request, 'mail_sender/registration.html')
