from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'manager'),
      (2, 'investigator'),
      (3, 'paralegal'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)