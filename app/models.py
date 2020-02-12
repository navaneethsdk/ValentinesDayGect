from django.db import models
from datetime import datetime

# Create your models here.


class RegisteredMembers(models.Model):
    name = models.CharField(max_length=32, blank=False, verbose_name="Name", help_text="Name of registrant")
    gender = models.BooleanField(blank=False, verbose_name="Gender", help_text="True for male, False for female")
    age = models.IntegerField(blank=False, verbose_name="Age")
    native_place = models.CharField(max_length=60, blank=False, verbose_name="Native Place", help_text="Native Place")
    phone_no = models.CharField(max_length=13, blank=False, verbose_name="Phone Number", help_text="Phone Number")
    blocked = models.BooleanField(default=False, verbose_name="Block this user", help_text="Block this user or not")
    unique_id = models.CharField(blank=False, max_length=15, verbose_name="Unique profile number")
    pair_unique_id = models.CharField(blank=True, max_length=15, verbose_name="Unique profile number of pair")
    remarks = models.TextField(max_length=161, blank=True, verbose_name="Department & Semester", help_text="Department & Semester")
    dob = models.DateField(blank=False, verbose_name="Date of Birth", default=datetime.now)
    interests = models.TextField(max_length=250, blank=False, default="")
    ktu_reg_no = models.CharField(max_length=11, verbose_name="Reg No", default="", blank=False)


class Interests(models.Model):
    interets = models.CharField(max_length=32, blank=False, verbose_name="Interest", help_text="Interests that we have")
    category = models.CharField(max_length=32, blank=False, verbose_name="Category", help_text="category of interests")
