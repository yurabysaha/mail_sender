from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import JobForm
from .models import Job
from email_service.models import Email


def job_list(request):
    jobs = Job.objects.filter(created_at__lte = timezone.now()).order_by('created_at')
    return render(request, 'job_list/job_list.html', {'jobs': jobs})


def job_delete(request, job_id):
    job = Job.objects.get(id = job_id)
    if request.method == "POST":
        job.delete()
        return redirect("jobs")

    context = {
    "object": job,
    }

    return render(request, "job_list/confirm_delete.html", context)


def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user.id
            form.save()
            return redirect('jobs')
    else:
        form = JobForm()
    return render(request, 'job_list/job_create.html', {'form': form})


def job_edit(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    else:
        form = JobForm(instance=job)
    return render(request, 'job_list/job_edit.html', {'form': form})


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_list/job_details.html', {'job': job})


