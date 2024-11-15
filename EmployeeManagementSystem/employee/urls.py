from django.contrib import admin
from django.urls import path
from myapp.views import employee_details
from myapp.views import employee_update
from myapp.views import employee_delete
from myapp.views import employee_add
from myapp.views import employee_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', employee_details.as_view(), name='home'),
    path('update/<int:id>/', employee_update.as_view(), name="update"),
    path('delete/<int:id>/', employee_delete.as_view(), name="delete"),
    path('add/', employee_add.as_view(), name="add"),
    path('employee_search/', employee_search.as_view(), name="search"),
]
