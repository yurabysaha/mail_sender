from .forms import UploadFileForm
from django.shortcuts import render, redirect, get_object_or_404
import csv
from email_service.models import Email
from job_board.models import Job
from .parsing_xlsx import parsing_xlsx
from .parsing_CSV_function import parsing_csv
from .hungle_upload_file import handle_uploaded_file

def upload_file(request, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id)

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_type = request.FILES['file'].name.split('.')[-1]
            if file_type == 'xlsx':
                parsed_data = parsing_xlsx(request.FILES['file'], request.FILES['file'].name.split('.')[0])

                for row in parsed_data:
                    email = Email(first_name=row["first_name"],
                              last_name=row["last_name"],
                              email=row['email_adress'],
                              job=job)
                    email.save()

            elif file_type == 'csv':
                handle_uploaded_file(request.FILES['file'], request.FILES['file'].name.split('.')[0])
                parsed_data = parsing_csv('./media/{}.csv'.format(request.FILES['file'].name.split('.')[0]))

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