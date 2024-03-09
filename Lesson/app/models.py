from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField("name", max_length = 20)
    surname = models.CharField("surname", max_length = 20)
    phone_number = models.CharField("phone_number", max_length = 13)
    photo = models.FileField("photo", upload_to = "upload/", null = True, blank = True)

