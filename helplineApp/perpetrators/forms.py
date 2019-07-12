from django import forms

from .models import Perpetrator

class PerpetratorModelForm(forms.ModelForm):
    class Meta:
        model = Perpetrator
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'location',
            'national_id_number'
        ]
