from django.db import models
from django import forms

# Create your models here.
class EmployeeModel(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    mobile = models.IntegerField()
    city = models.CharField(max_length=20)