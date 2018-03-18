from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Job


def job_list(request):
    jobs = Job.objects.filter(created_at__lte = timezone.now()).order_by('created_at')
    return render(request, 'job_list/job_list.html', {'jobs': jobs})


def job_delete(request, job_id):
    job = Job.objects.get(id = job_id)
    job.delete()
    return redirect("/jobs/")
