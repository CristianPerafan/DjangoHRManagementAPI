from django.urls import path
from . import views

urlpatterns = [
    path('registerEmployee', views.registerEmployee,name='registerEmployee'),
    path('login', views.login,name='login'),
    path('testtoken', views.test_token,name='test_token'),
    path('logout', views.logout,name='logout'),
]