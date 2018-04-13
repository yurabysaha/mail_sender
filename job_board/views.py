from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.utils import timezone
from .forms import JobForm, AddEmailForm
from .models import Job
from user_profile.models import MyUser
from email_service.models import Email
import csv
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def job_list(request):
    if request.user.is_authenticated:
        query = request.GET.get('q')
        if query:
            jobs = Job.objects.filter(title__icontains=query)
            return render(request, 'job_list/job_list.html', {'jobs': jobs})
        jobs_list = Job.objects.filter(user=request.user)
        paginator = Paginator(jobs_list, 25)

        page = request.GET.get('page')

        jobs = paginator.get_page(page)
        return render(request, 'job_list/job_list.html', {'jobs': jobs})
    else:
        return redirect('/')



def job_delete(request, job_id):
    if request.user.is_authenticated:
        job = Job.objects.get(id=job_id)
        if request.method == "POST":
            job.delete()
            return redirect("jobs")

        context = {
        "object": job,
        }

        return render(request, "job_list/job_list.html", context)
    else:
        return redirect('/')


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
        return redirect('/')


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
        return redirect('/')


def job_detail(request, job_id):
    if request.user.is_authenticated:

        job = get_object_or_404(Job, id=job_id)
        emails_list = Email.objects.all().filter(job=job)

        paginator = Paginator(emails_list, 25)
        page = request.GET.get('page')
        emails = paginator.get_page(page)

        return render(request, 'job_list/job_details.html', {'job': job, 'emails': emails})
    else:
        return redirect('/')


def add_email(request, job_id):
    if request.user.is_authenticated:
          job = get_object_or_404(Job, id=job_id)
          if request.method == "POST":
              email = Email(email=request.POST['email'],
                            first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            job=job)
              form = AddEmailForm(request.POST, instance=email)
              if form.is_valid():
                  form.save()
                  return redirect('/jobs/{}'.format(job_id))
          else:
              form = AddEmailForm(instance=job)
              return render(request, 'job_list/job_add_email.html', {'form': form})
    else:
        return redirect('login')


def edit_email(request, email_id, job_id):
    if request.user.is_authenticated:

        email = get_object_or_404(Email, id=email_id)
        if request.method == "POST":
            form = AddEmailForm(request.POST, instance=email)
            if form.is_valid():
                form.save()
                return redirect('/jobs/{}'.format(job_id))
        else:
            form = AddEmailForm(instance=email)
            return render(request, 'job_list/job_email_edit.html', {'form': form})

    else:
        return redirect('login')


def delete_email(request, email_id, job_id):
    if request.user.is_authenticated:
        email = get_object_or_404(Email, id=email_id)
        if request.method == "POST":
            email.delete()
            return redirect('/jobs/{}'.format(job_id))

        return render(request, "job_list/job_details.html", context)

    else:
        return redirect('login')


def export_to_csv_email(request, job_id):
    if request.user.is_authenticated:

        job = get_object_or_404(Job, id=job_id)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="emails_{}.csv"'.format(job.title)

        field_names = ['First_Name', 'Last_Name', 'Email']

        writer = csv.DictWriter(response, fieldnames=field_names, delimiter=';')
        writer.writeheader()

        emails = Email.objects.values_list('email', 'first_name', 'last_name').filter(job=job)

        for email in emails:
            writer.writerow({'First_Name' : email[0], 'Last_Name' : email[1], 'Email' : email[2]})

        return response

    else:
        return redirect('login')

