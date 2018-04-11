from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name = "jobs"),
    path('<int:job_id>/delete/', views.job_delete),
    path('create', views.job_create, name = "create job"),
    path('<int:job_id>/edit', views.job_edit),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('<int:job_id>/add_email/', views.add_email, name='add_email'),
    path('<int:job_id>/edit_email/<int:email_id>', views.edit_email, name='edit_email'),
    path('<int:job_id>/<int:email_id>/delete/', views.delete_email, name='delete_email'),
    path('<int:job_id>/upload/', upload_file),
    path('<int:job_id>/export/', views.export_to_csv_email, name='export_to_csv_email'),
]
