from django import forms
from .models import Employee

class EmployeeInfoForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        labels={
            "fname":"First Name",
            "lname":"Last Name",
            "age":"Age",
            "address":"Address"
        }
        widgets={
            "fname":forms.TextInput(attrs={"class":"form-control"}),
            "lname":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"})
        }