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
        jobs = Job.objects.filter(user=request.user)
        return render(request, 'job_list/job_list.html', {'jobs': handle_pagination(request, jobs)})
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

#TODO add this method to another "Help functions" file
def handle_pagination(request, data_to_paginate):
    paginator = Paginator(data_to_paginate, 25)
    page = request.GET.get('page')
    paginated_page = paginator.get_page(page)

    return paginated_page


def job_detail(request, job_id):
    if request.user.is_authenticated:
        job = get_object_or_404(Job, id=job_id)
        emails_list = Email.objects.order_by('first_name').filter(job=job)

        form = AddEmailForm()

        if 'order_by' in request.GET:
            order_by = request.GET.get('order_by')
            sorted_emails = Email.objects.order_by(order_by).filter(job=job)

            return render(request, 'job_list/job_details.html', {'job': job,
                                                             'emails': handle_pagination(request,
                                                                                         sorted_emails)})
        else:
            return render(request, 'job_list/job_details.html', {'job': job,
                                                                 'emails': handle_pagination(request,
                                                                                             emails_list)})
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
        return redirect('/')


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
        return redirect('/')


def delete_email(request, email_id, job_id):
    if request.user.is_authenticated:
        email = get_object_or_404(Email, id=email_id)
        if request.method == "POST":
            email.delete()
            return redirect('/jobs/{}'.format(job_id))

        return render(request, "job_list/job_details.html", context)

    else:
        return redirect('/')


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
        return redirect('/')

