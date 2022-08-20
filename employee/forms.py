from django import forms
from employee.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets={
            "eid":forms.TextInput(attrs={"class":"form-control"}),
            "employee_name":forms.TextInput(attrs={"class":"form-control"}),
            "designation":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "experience":forms.NumberInput(attrs={"class":"form-control"})
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name",
                "last_name",
                "email",
                "username",
                "password1",
                "password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


