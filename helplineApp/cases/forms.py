from django import forms

from .models import Case

class CaseModelForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'victim',
            'perpetrator',
            'reported_case',
            'location',
            'reported_to',
            'case_no',
            'lawyer',
            'police_station',
            'court'
        ]
