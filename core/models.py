from django.db import models
from django.utils import timezone
# Create your models here.

from django.utils import timezone

class Invitation(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Birthday(models.Model):
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    message = models.TextField(blank=True)
    photo = models.ImageField(upload_to='birthdays/', blank=True, null=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=250, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
