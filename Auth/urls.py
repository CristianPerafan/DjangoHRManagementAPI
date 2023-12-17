from django.urls import path
from . import views

urlpatterns = [
    path('assing-user', views.AssignUserToEmployee.as_view(), name='assing-user'),
]