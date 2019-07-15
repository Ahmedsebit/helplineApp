from django.core.exceptions import ValidationError
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.db import models

# Create your models here.
class Victim(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    date_of_birth = models.DateField()


    def clean(self):
        if self.date_of_birth >= timezone.now().date():
            raise ValidationError('The date seems to be wrong')

    def __str__ (self):
        return str(self.first_name)
