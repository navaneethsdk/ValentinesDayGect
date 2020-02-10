from django.shortcuts import render, HttpResponse
import datetime
from .models import *
# Create your views here.


def home(request):
    return render(request, 'index.html')


def form(request):
    if request.method == "GET":
        return render(request, 'form.html')
    elif request.method == "POST":
        name = request.POST['name']
        if request.POST['gender'] == "1":
            gender = True
        else:
            gender = False
        age = request.POST['age']
        dob = request.POST['dob']
        dob = datetime.strptime(dob, '%Y-%m-%d')
        native_place = request.POST['native_place']
        phmob = request.POST['phmob']
        remarks = request.POST['remarks']
        event = RegisteredMembers.objects.create(name=name, gender=gender, age=age, dob=dob, native_place=native_place, phone_no=phmob, remarks=remarks, unique_id=phmob)
        event.save()
        # print(gender)
        return HttpResponse("Success")