from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone

from job_board.forms import JobForm
from .models import Job


def job_list(request):
    jobs = Job.objects.filter(created_at__lte = timezone.now()).order_by('created_at')
    return render(request, 'job_list/job_list.html', {'jobs': jobs})


def job_delete(request, job_id):
    job = Job.objects.get(id = job_id)
    job.delete()
    return redirect("/jobs/")


def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = User.objects.first().id
            form.save()
            return redirect('jobs')
    else:
        form = JobForm()
    return render(request, 'job_list/job_create.html', {'form': form})
