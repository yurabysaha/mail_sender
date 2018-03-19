from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
]
