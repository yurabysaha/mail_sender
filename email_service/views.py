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
            parsing_xlsx(request.FILES['file'], request.POST['title'])

            data = csv.reader(open('./media/{}.csv'.format(request.POST['title'])), delimiter=",")
            for row in data:
                email = Email(first_name=row[0],
                              last_name=row[1],
                              email=row[2],
                              job=job)
                email.save()

            return redirect('/jobs/{}'.format(job_id))

    else:
        form = UploadFileForm()

    return render(request, "job_list/upload.html", {'form': form})