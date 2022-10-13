from email.headerregistry import Address
from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from myapp.models import fruit
import json




# Create your views here
def index(request):
    return render(request,'id/home.html',context={})

def login(request):
    return render(request,'id/login.html',context={})

def table(request):
    return render(request,'id/table.html',context={})

def welcome(request):
    return render(request,'id/welcome.html',context={})




def form_data(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        Phone = request.POST['phone']
        # Address = request.POST['address']
        Email = request.POST['email']
        Password = make_password(request.POST['Password'])
        if fruit.objects.filter(first_name=first_name).exists():
            messages.error(request,"first_name is already exists")
            return redirect('/')

        elif fruit.objects.filter(Email=Email).exists():
            messages.error(request,"phone no. is already exists")
            return redirect('/')

        else:
            fruit.objects.create(first_name=first_name ,Email= Email,
                                    Password=Password,Phone=Phone,last_name=last_name)
            return redirect('/login/')

def Login_form(request):
    if request.method == 'POST':
        Email = request.POST['email']
        user_Password = request.POST['Password']
        if fruit.objects.filter(Email=Email).exists():
            obj=fruit.objects.get(Email=Email)
            password=obj.Password
            if check_password(user_Password,password):
                return redirect('/welcome/')
            else:
                return HttpResponse("Password incorrect")
    else:
            return HttpResponse("email is not registerd")


def data(request):
    persons=fruit.objects.filter(is_active=True).order_by('id')
    return render(request,'id/table.html',context={
        'request' : request,
        'persons' : persons,
    })

def delete_user(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        uid = json.loads(data)
        if fruit.objects.filter(id=uid).exists():
            fruit.objects.filter(id=uid).update(is_active=False)
            return JsonResponse({"staus": True, "message" : "user has been delete"})
        else:
            return JsonResponse({"staus": False, "message" : "user not exists"})
    else:
        return JsonResponse({"staus": False, "message" : "Method not allowed"})


def update_view(request,uid):
    res = fruit.objects.get(id=uid)
    return render(request,'id/update.html',context={
        'person': res,
    }) 
            
def update_form_data(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Phone = request.POST['Phone']
        #Address = request.POST['Address']
        Email = request.POST['Email']
        Password = request.POST['Password']
        fruit.objects.filter(id=uid).update(first_name=first_name,
                                    last_name=last_name,Phone=Phone,
                                    Email=Email,Password=Password)
        return redirect('/data/')

def delete_user(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        uid = json.loads(data)
        if fruit.objects.filter(id=uid).exists():
            fruit.objects.filter(id=uid).update(is_active=False)
            return JsonResponse({"staus": True, "message" : "user has been delete"})
        else:
            return JsonResponse({"staus": False, "message" : "user not exists"})
    else:
        return JsonResponse({"staus": False, "message" : "Method not allowed"})
    
