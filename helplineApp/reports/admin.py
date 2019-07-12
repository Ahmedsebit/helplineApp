from django.contrib import admin

# Register your models here.
from .forms import ReportModelForm
from .models import Report

# admin.site.register(Tweet)

class ReportModelAdmin(admin.ModelAdmin):
    form = ReportModelForm
    class meta:
        model = Report
        
admin.site.register(Report, ReportModelAdmin)
