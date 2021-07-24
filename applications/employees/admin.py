from django.contrib import admin

# Register your models here.
from applications.employees.models import Employee

admin.site.register(Employee)
