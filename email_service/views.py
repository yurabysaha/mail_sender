from .forms import UploadFileForm
from django.shortcuts import render, redirect, get_object_or_404
from job_board.views import add_email
from .parsing_xlsx import parsing_xlsx
import csv
from email_service.models import Email
from job_board.models import Job



# def upload_file(request, job_id):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             parsing_xlsx(request.FILES['file'])
#             return render(request, "job_list/job_details.html")
#     else:
#         form = UploadFileForm()
#
#     return render(request, "job_list/upload.html", {'form': form})



def add_email(request, job_id):
    data = csv.reader(open("/Users/viktorgrigorevskiy/Desktop/projects/mail_sender/created.csv"), delimiter=",")
    job = get_object_or_404(Job, id=job_id)

    for row in data:
        email = Email(first_name=row[0],
                      last_name=row[1],
                      email=row[2],
                      job=job)

        email.save()
    return render(request, "job_list/job_details.html")
