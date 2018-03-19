from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),

]