from django.shortcuts import render
from .forms import CustomUserCreationForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import forms  
from django.shortcuts import redirect 
from django.contrib import messages  

from ast import Return
from enum import Flag

from .forms import BookingForm

from .models import Departments, Doctors,CustomUser


# Create your views here.


def about(request):
    return render(request,'about.html')


  
def signup(request):
    form=CustomUserCreationForm()
    if(request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'signup.html',{"form":form})


def user_login(request):
    if(request.method=='POST'):
        name=request.POST['n']
        password=request.POST['p']
        user=authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('Invalid .......... NO user found !')
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return user_login(request)


def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)
        

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)