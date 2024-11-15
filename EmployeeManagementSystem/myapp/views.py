from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Employee
from .forms import EmployeeInfoForm
from django.db.models import Q
from django.views import View


class employee_details(View):
    def get(self, request):
        # Get all employees from the database
        employees = Employee.objects.all().values()
        return render(request, 'employee_details.html', {"employee": employees})


class employee_update(View):
    def get(self, request, id):
        # Fetch the employee record
        employee = Employee.objects.get(pk=id)
        fm = EmployeeInfoForm(instance=employee)
        return render(request, "employee_update.html", {"form": fm})

    def post(self, request, id):
        # Handle the form submission
        employee = Employee.objects.get(pk=id)
        fm = EmployeeInfoForm(request.POST, instance=employee)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/home")
        return render(request, "employee_update.html", {"form": fm})


class employee_delete(View):
    def post(self, request, id):
        # Delete the employee record
        employee = Employee.objects.get(pk=id)
        employee.delete()
        return HttpResponseRedirect("/home")


class employee_add(View):
    def get(self, request):
        fm = EmployeeInfoForm()
        return render(request, "employee_add.html", {"form": fm})

    def post(self, request):
        fm = EmployeeInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/home")
        return render(request, "employee_add.html", {"form": fm})


class employee_search(View):
    def get(self, request):
        # Handle search results for GET requests
        return render(request, "employee_search.html")

    def post(self, request):
        search = request.POST.get("output")
        employees = Employee.objects.all()
        sta = None
        if search:
            sta = employees.filter(
                Q(fname__icontains=search) |
                Q(lname__icontains=search) |
                Q(age__icontains=search) |
                Q(address__icontains=search)
            )
        return render(request, "employee_details.html", {"employee": sta})
