from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField('name', max_length=20)
    last_name=models.CharField('last_name', max_length=20)
    number=models.CharField('number', max_length=14)
