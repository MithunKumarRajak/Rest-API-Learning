from rest_framework import serializers
from employee.models import Employee
from students.models import Student


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

