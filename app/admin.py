from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(RegisteredMembers)
class RegisteredMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'native_place', 'blocked']
