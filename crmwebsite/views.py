from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from . forms import SignUpForm,AddUserForm
from . models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user  = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged In")
            return redirect('home')
        else:
            messages.success(request,"There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request,'crmwebsite/home.html',{'records':records})


def logout_user(request):
     logout(request)
     messages.success(request, "You have Been Logged Out..")
     return redirect('home')

def register_user(request):
    if request.method == "POST":
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:

        form = SignUpForm()
        return render(request,"crmwebsite/register.html",{'form':form})
    
    return render(request,"crmwebsite/register.html",{'form':form})


def user_record(request,pk):
    if request.user.is_authenticated:
        user_record = Record.objects.get(id=pk)
        return render(request,"crmwebsite/record.html",{'user_record':user_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete  = Record.objects.get(id=pk)
        delete.delete()
        messages.success(request, "Record Deleted Successfully....")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To do That....")
        return redirect('home')

def add_user(request):
    form = AddUserForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_user = form.save()
                messages.success(request,"Record Added....")
                return redirect('home')
        return render(request,"crmwebsite/add_user.html",{'form':form})
    else:
        messages.success(request,"You Must be Logged In")
        return redirect('home')
    

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddUserForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has Been Updated....")
            return redirect('home')
        return render(request,"crmwebsite/update_user.html",{'form':form})
        
    else:
         messages.success(request,"You Must be Logged In")
         return redirect('home')




