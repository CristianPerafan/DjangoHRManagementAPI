from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register,name='register'),
    path('login', views.login,name='login'),
    path('testtoken', views.test_token,name='test_token'),
]