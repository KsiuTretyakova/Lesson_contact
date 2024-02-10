from django.db import models

class Contact(models.Model):
    name = models.CharField('name', max_length=20)
    last_name = models.CharField('last_name', max_length=20)
    number = models.CharField('number', max_length=15)
    photo = models.FileField('photo',
                             upload_to='images/img_contact/',
                             null=True,
                             blank=True)

    def __str__(self):
        return f'{self.name} {self.number}'