from django.db import models

# Create your models here.
class Perpetrator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    national_id_number = models.CharField(max_length=200)

    def __str__ (self):
        return str(self.first_name)
