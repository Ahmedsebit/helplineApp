from django.db import models
from reports.models import Report
from victims.models import Victim
from perpetrators.models import Perpetrator
from incidences.models import Incidence
from users.models import User

# Create your models here.
class Case(models.Model):
    incidence = models.ForeignKey(Incidence, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    location = models.CharField(max_length=20)
    reported_to = models.CharField(max_length=20)
    case_no = models.CharField(max_length=20)
    lawyer = models.CharField(max_length=20)
    police_station = models.CharField(max_length=20)
    court = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    # class Meta:
    #     unique_together = (('victim','reported_case'),('reported_case','perpetrator'),('victim','incidence'))

    # def __str__ (self):
    #     return str(self.ref)

    # def get_absolute_url(self):
    #     return u'/payment/%d/' % self.ref