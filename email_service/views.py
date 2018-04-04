from .forms import UploadFileForm
from django.shortcuts import render, redirect, get_object_or_404

# Imaginary function to handle an uploaded file.
def handle_uploaded_file(file, filename):
    if not os.path.exists('media/'):
        os.mkdir('media/')

    with open('media/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request, job_id):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])

            return render(request, "job_list/job_details.html")
    else:
        form = UploadFileForm()

    return render(request, "job_list/job_details.html", {'form': form})
