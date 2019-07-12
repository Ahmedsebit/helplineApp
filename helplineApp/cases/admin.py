from django.contrib import admin

# Register your models here.
from .forms import CaseModelForm
from .models import Case

# admin.site.register(Tweet)

class CaseModelAdmin(admin.ModelAdmin):
    form = CaseModelForm
    class meta:
        model = Case
        
admin.site.register(Case, CaseModelAdmin)

