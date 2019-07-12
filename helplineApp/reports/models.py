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

    def __str__ (self):
        return str(self.info)
