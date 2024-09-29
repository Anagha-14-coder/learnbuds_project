from django.db import models

# Create your models here.
class employee_db(models.Model):
    employee_name=models.CharField(max_length=200)
    employee_category=models.CharField(max_length=200)
    employee_phone=models.CharField(max_length=12)
    employee_dob=models.CharField(max_length=10)
    employee_gender=models.IntegerField(choices=[(1,'male'),(2,'female'),(3,'other')])
    employee_address=models.CharField(max_length=500)
    employee_email=models.CharField(max_length=200)
    employee_qualification=models.CharField(max_length=100)