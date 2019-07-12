from django.contrib import admin

# Register your models here.
from .forms import PerpetratorModelForm
from .models import Perpetrator

# admin.site.register(Tweet)

class PerpetratorModelAdmin(admin.ModelAdmin):
    form = PerpetratorModelForm
    class meta:
        model = Perpetrator
        
admin.site.register(Perpetrator, PerpetratorModelAdmin)
