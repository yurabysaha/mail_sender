from .forms import UploadFileForm
from django.shortcuts import render, redirect, get_object_or_404
from job_board.views import add_email
from .parsing_xlsx import parsing_xlsx
import csv
from email_service.models import Email
from job_board.models import Job


def handle_uploaded_file(f, title):
    with open('/Users/viktorgrigorevskiy/Desktop/projects/mail_sender/media/{}.csv'.format(title), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request, job_id):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.POST['title'])

            data = csv.reader(open("/Users/viktorgrigorevskiy/Desktop/projects/mail_sender/created.csv"), delimiter=",")
            job = get_object_or_404(Job, id=job_id)

            for row in data:
                email = Email(first_name=row[0],
                              last_name=row[1],
                              email=row[2],
                              job=job)
                email.save()

            return render(request, "job_list/job_details.html", {'job':job})

    else:
        form = UploadFileForm()

    return render(request, "job_list/upload.html", {'form': form})
