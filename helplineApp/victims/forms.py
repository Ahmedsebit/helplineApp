from django import forms

from .models import Victim

class VictimModelForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'location',
            'date_of_birth'
        ]
