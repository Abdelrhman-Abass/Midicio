from django.db import models


# Create your models here.
class Apointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length= 100)
    phone_number = models.CharField(max_length=25)
    date = models.DateField()
    doctor = models.ForeignKey('Doctor' , on_delete=models.CASCADE)
    department =models.ForeignKey('Department', on_delete=models.CASCADE)


    def __str__(self):
        return f"Name pationt is  {self.name} ----  Doctor name is    {self.doctor}  ----   Date is      {self.date}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


