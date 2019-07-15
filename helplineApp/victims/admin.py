from django.contrib import admin

# Register your models here.
from .forms import VictimModelForm
from .models import Victim

class VictimModelAdmin(admin.ModelAdmin):
    form = VictimModelForm
    class meta:
        model = Victim
        
admin.site.register(Victim, VictimModelAdmin)
