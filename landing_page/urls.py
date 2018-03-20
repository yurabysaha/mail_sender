from django.urls import path
from landing_page import views

urlpatterns =[
    path('', views.index_page, name = "index")
]
