from django.db import models

# Create your models here.

class Code_Phone_Country(models.Model):
    name_ES = models.CharField(max_length=100)
    name_EN = models.CharField(max_length=100)
    ISO_2 = models.CharField(max_length=10)
    ISO_3 = models.CharField(max_length=10)
    code_phone = models.CharField(max_length=10)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)