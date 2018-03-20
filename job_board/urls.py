from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name = "jobs"),
    path('<int:job_id>/delete/', views.job_delete),
    path('create', views.job_create, name = "create job"),
    path('<int:job_id>/edit', views.job_edit),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
]


