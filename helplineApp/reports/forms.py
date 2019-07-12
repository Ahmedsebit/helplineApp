from django import forms

from .models import Report

class ReportModelForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'info',
            'report_date',
            'case_opened'
        ]
