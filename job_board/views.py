from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import JobForm
from .models import Job


def job_list(request):
    if request.user.is_authenticated:
        jobs = Job.objects.filter(created_at__lte = timezone.now()).order_by('created_at')
        return render(request, 'job_list/job_list.html', {'jobs': jobs})
    else:
        return redirect('login')


def job_delete(request, job_id):
    if request.user.is_authenticated:

        job = Job.objects.get(id = job_id)
        if request.method == "POST":
            job.delete()
            return redirect("jobs")

        context = {
        "object": job,
        }

        return render(request, "job_list/job_list.html", context)

    else:
        return redirect('login')


def job_create(request):
    if request.user.is_authenticated:

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

    else:
        return redirect('login')


def job_edit(request, job_id):
    if request.user.is_authenticated:

        job = get_object_or_404(Job, id=job_id)
        if request.method == "POST":
            form = JobForm(request.POST, instance=job)
            if form.is_valid():
                form.save()
                return redirect('jobs')
        else:
            form = JobForm(instance=job)
        return render(request, 'job_list/job_edit.html', {'form': form})
    else:
        return redirect('login')


def job_detail(request, job_id):
    if request.user.is_authenticated:

        job = get_object_or_404(Job, id=job_id)
        return render(request, 'job_list/job_details.html', {'job': job})
    else:
        return redirect('login')

