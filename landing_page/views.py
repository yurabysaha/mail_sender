from django.shortcuts import render, redirect


def index_page(request):
    if request.user.is_authenticated:
        return redirect("jobs")
    return render(request, 'index.html', {})
