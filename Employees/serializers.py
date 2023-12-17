from rest_framework import serializers
from .models import Employee, Gender, Role

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['name']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']