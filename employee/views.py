from django.shortcuts import render
from employee.forms import EmployeeCreateForm
from django.views.generic import View
from employee.models import Employee
from django.contrib import messages
from django.shortcuts import redirect
from employee.forms import UserRegistrationForm
from employee.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.utils .decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("sign-in")
    return wrapper

@method_decorator(signin_required,name="dispatch")
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeCreateForm()
        return render(request,"emp-add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request,"employee has been added")
            return render(request,"emp-add.html", {"form": form})
        else:
            messages.error(request,"employee added failed")
            return render(request,"emp-add.html", {"form": form})

@method_decorator(signin_required,name="dispatch")
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            qs=Employee.objects.all()
            return render(request,"emp-list.html",{"employees":qs})
        else:
            return redirect("sign-in")

@method_decorator(signin_required,name="dispatch")
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.get(eid=kwargs.get("emp_id"))
        return render(request,"emp-detail.html",{"employee":qs})


class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request,"emp-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(eid=eid)
        form = EmployeeCreateForm(request.POST,instance=employee,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "employee has been updated")
            return render(request, "emp-list.html", {"form": form})
        else:
            messages.error(request, "employee added failed")
            return render(request, "emp-add.html", {"form": form})


def remove_employee(request,*args,**kwargs):
    eid=kwargs.get("e_id")
    employee=Employee.objects.get(eid=eid)
    employee.delete()
    messages.error(request,"employee has been removed")
    return redirect("emp-list")

@method_decorator
def index(request):
    return render(request,"base.html")

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created")
            return redirect("sign-in")
        else:
            messages.error(request, "account creation has been failed")
            return render(request,"registration.html",{"form":form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm
        return render(request,"log_in.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pw=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pw)
            if user:
                login(request,user)
                print("success")
                return redirect("emp-list")
            else:
                messages.error(request,"invalid credentials")
                return render(request, "log_in.html", {"form": form})

def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("sign-in")
