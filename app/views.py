from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import *
# Create your views here.

import random
import string


def home(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        profile = request.POST['profile']
        try:
            e = RegisteredMembers.objects.get(phone_no=profile)
            return HttpResponse('success')
        except:
            return HttpResponse('failed')


def form(request):
    if request.method == "GET":
        analyzer()
        data = Interests.objects.all()
        return render(request, 'form.html', {'data': data})
    elif request.method == "POST":
        try:
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
            interests = request.POST['interests']
            ktu_reg_no = request.POST['reg_no']
            flag = False
            # try:
            #     e = RegisteredMembers.objects.get(ktu_reg_no=ktu_reg_no)

            # except:
            e = RegisteredMembers.objects.filter(ktu_reg_no=ktu_reg_no).count()
            f = RegisteredMembers.objects.filter(name=name).count()
            g = RegisteredMembers.objects.filter(phone_no=phmob).count()
            # print(e)
            if e <= 0 and f <= 0 and g <= 0:
                event = RegisteredMembers.objects.create(
                    ktu_reg_no=ktu_reg_no,
                    name=name,
                    gender=gender,
                    age=age, dob=dob,
                    native_place=native_place,
                    phone_no=phmob,
                    remarks=remarks,
                    unique_id=phmob+randomString(4),
                    interests=interests
                )
                event.save()
                flag = True
            # print(gender)
            if flag:
                return HttpResponse("Success")
            else:
                return HttpResponse("Unsuccessful")
        except:
            return HttpResponse("Unsuccessful")


def analyzer():
    boys = RegisteredMembers.objects.filter(gender=True)
    girls = RegisteredMembers.objects.filter(gender=False)
    all_inter = []
    data = Interests.objects.all()
    for i in data:
        all_inter.append(i.interets)
    # print(all_inter)

    boys_list = []
    for i in boys:
        b_bin = ""
        inter = i.interests
        inter = inter.split('$$')
        inter.pop(0)
        for j in all_inter:
            if j in inter:
                b_bin += '1'
            else:
                b_bin += '0'
        boys_list.append((i, b_bin))
    # print(boys_list)

    girls_list = []
    for i in girls:
        g_bin = ""
        inter = i.interests
        inter = inter.split('$$')
        inter.pop(0)
        for j in all_inter:
            if j in inter:
                g_bin += '1'
            else:
                g_bin += '0'
        girls_list.append((i, g_bin))

    pair_list = []
    for i in boys_list:
        for j in girls_list:
            print(girls_list)
            b = int(i[1], 2)
            g = int(j[1], 2)
            combine = bin(b & g)
            if combine != bin(0):
                # i[0].pair_unique_id = j[0].unique_id
                girls_list.remove(j)
                print(girls_list)
                pair_list.append((i[0], j[0]))
                break
    print(pair_list)
    for i in pair_list:
        i[0].pair_unique_id = i[1].unique_id
        i[1].pair_unique_id = i[0].unique_id
        i[0].save()
        i[1].save()


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def getProfile(request, foo):
    data = RegisteredMembers.objects.get(phone_no=foo)
    return render(request, 'profile.html', {'data': data})


def scratchcard(request,foo):
    event = RegisteredMembers.objects.get(phone_no=foo)
    data = RegisteredMembers.objects.get(unique_id=event.pair_unique_id)
    inter = data.interests
    list_inter = inter.split('$$')
    inter = ""
    for i in list_inter[1:]:
        inter += i + ", "
    inter = inter[:-2]
    return render(request, 'scratchcard.html', {'data': data, 'inter': inter})

def pairProfile(request, foo):
    data = RegisteredMembers.objects.get(phone_no=foo)
    return render(request, 'pair_profile.html', {'data': data})

