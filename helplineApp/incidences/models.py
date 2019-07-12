from django.db import models
from reports.models import Report
from victims.models import Victim
from perpetrators.models import Perpetrator
from users.models import User

# Create your models here.
class Incidence(models.Model):
    YES = 'yes'
    NO = 'no'

    FR = 'FR'
    DAFR_OR_IR = 'DAFR_OR_IR'

    PERITRAUMATIC_FEAR = [
        (YES, 'yes'),
        (NO, 'no'),
    ]
    INJURY = [
        (YES, 'yes'),
        (NO, 'no'),
    ]
    RAPE_TYPE = [
        (FR, 'FR'),
        (DAFR_OR_IR, 'DAFR_OR_IR'),
    ]
    MEMORY_OF_RAPE = [
        (YES, 'yes'),
        (NO, 'no'),
    ]
    PERPETRATOR_INTIMATE_PARTNER = [
        (YES, 'yes'),
        (NO, 'no'),
    ]
    PERPETRATOR_A_STRANGER = [
        (YES, 'yes'),
        (NO, 'no'),
    ]
    PRIOR_RAPE_HISTORY = [
        (YES, 'yes'),
        (NO, 'no'),
    ]
    HISTORY_OF_PREVIOUS_RAPE  = [
        (YES, 'yes'),
        (NO, 'no'),
    ]

    peritraumatic_fear = models.CharField(
        max_length=2,
        choices=PERITRAUMATIC_FEAR,
        default=NO,
    )
    injury = models.CharField(
        max_length=2,
        choices=INJURY,
        default=NO,
    )	
    rape_type = models.CharField(
        max_length=2,
        choices=RAPE_TYPE,
        default=FR,
    )
    memory_of_rape = models.CharField(
        max_length=2,
        choices=INJURY,
        default=NO,
    )
    perpetrator_intimate_partner = models.CharField(
        max_length=2,
        choices=PERPETRATOR_INTIMATE_PARTNER,
        default=NO,
    )
    perpetrator_a_stranger = models.CharField(
        max_length=2,
        choices=PERPETRATOR_A_STRANGER,
        default=NO,
    )
    prior_rape_history = models.CharField(
        max_length=2,
        choices=PRIOR_RAPE_HISTORY,
        default=NO,
    )
    history_of_previous_rape = models.CharField(
        max_length=2,
        choices=HISTORY_OF_PREVIOUS_RAPE,
        default=NO,
    )
    investigator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    # def __str__ (self):
    #     return str(self.investigator)

    # def get_absolute_url(self):
    #     return u'/incidences/%d/' % self.investigator