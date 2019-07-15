from django import forms

from .models import Case

class CaseModelForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'incidence',
            'location',
            'reported_to',
            'case_no',
            'lawyer',
            'police_station',
            'court'
        ]
