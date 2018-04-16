from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('me/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password')
]
