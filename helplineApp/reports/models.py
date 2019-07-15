from django.core.exceptions import ValidationError
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.db import models
# Create your models here.

class Report(models.Model):
    info = models.CharField(max_length=200)
    report_date = models.DateTimeField(blank=True)
    YES = 'yes'
    NO = 'no'
    CASE_OPENED = [
        (YES, 'yes'),
        (NO, 'no')
    ]
    case_opened = models.CharField(
        max_length=2,
        choices=CASE_OPENED,
        default=NO,
    )

    def clean(self):
        if self.report_date <= timezone.now():
            raise ValidationError('The date seems to be wrong')
        if self.case_opened == 'yes':
            raise ValidationError('The report created and opened')

    def __str__ (self):
        return str(self.info)
