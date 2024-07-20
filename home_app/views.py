from home_app.models import registration_table
from home_app.models import login_table
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        city=request.POST['city']
        state=request.POST['state']
        zip_code=request.POST['zip']
        #make the variable and the objects
        reg_val=registration_table(fname=fname,lname=lname,email=email,city=city,state=state,zip=zip_code)
        reg_val.save()
    return render(request,"registration.html")

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        #make the variable and the objects
        log_val=login_table(email=email,password=password)
        log_val.save()

    return render(request,"login.html")
