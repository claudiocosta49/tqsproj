from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image


class Service(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    def __str__(self):
        return self.name



class Employee(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    birthdate = models.DateField(max_length=8)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to="user_images", blank=True)
    phone = models.CharField(max_length=30, default='')
    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        super().save()

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
