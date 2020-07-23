from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(RegisteredMembers)
class RegisteredMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'age', 'native_place', 'blocked', 'ktu_reg_no']


@admin.register(Interests)
class RegisteredMemberAdmin(admin.ModelAdmin):
    list_display = ['interets', 'category']
