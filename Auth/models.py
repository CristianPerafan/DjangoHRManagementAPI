from django.db import models
from django.contrib.auth.models import AbstractUser
from Employees.models import Employee

# Create your models here.
class CustomUser(AbstractUser):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)

    