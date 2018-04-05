from .forms import UploadFileForm
from django.shortcuts import render, redirect, get_object_or_404
import csv
from email_service.models import Email
from job_board.models import Job
from .parsing_xlsx import parsing_xlsx


def upload_file(request, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id)

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            parsed_data = parsing_xlsx(request.FILES['file'], request.FILES['file'].name.split('.')[0])

            for row in parsed_data:
                email = Email(first_name=row["first_name"],
                              last_name=row["last_name"],
                              email=row['email_adress'],
                              job=job)
                email.save()

            return redirect('/jobs/{}'.format(job_id))

    else:
        form = UploadFileForm()

    return render(request, "job_list/upload.html", {'form': form})