from django.db import models

# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Gender(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Employee(models.Model):

    id = models.CharField(max_length=10,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    gender = models.ForeignKey(Gender,on_delete=models.PROTECT)
    role = models.ForeignKey(Role,on_delete=models.PROTECT)

    adress = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


    
    def __str__(self):
        return self.name
