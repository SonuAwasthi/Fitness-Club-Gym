from django.db import models

# Create your models here.

class Membars(models.Model):
    indx=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=120)
    number=models.CharField(max_length=120)
    gmail=models.CharField(max_length=120)
    packages=models.CharField(max_length=120)
    gender=models.CharField(max_length=120)