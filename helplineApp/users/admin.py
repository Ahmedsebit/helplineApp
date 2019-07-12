from django.contrib import admin

# Register your models here.
from .forms import UserModelForm
from .models import User

# admin.site.register(Tweet)

class UserModelAdmin(admin.ModelAdmin):
    form = UserModelForm
    class meta:
        model = User
        
admin.site.register(User, UserModelAdmin)

