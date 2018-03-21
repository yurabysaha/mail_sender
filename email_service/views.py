from django.shortcuts import render
from django.utils import timezone
from email_service.models import Email


def email_list(request):
    emails = Email.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'job_list/job_details.html', {"emails": emails})