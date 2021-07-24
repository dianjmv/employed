from django.db import models

# Create your models here.
from applications.departments.models import Department


class Employee(models.Model):
    """Model of employees"""
    TYPE_JOBS = (
        ('0', 'Accountant'),
        ('1', 'Developer'),
        ('2', 'Manager')
    )
    first_name = models.CharField('Name', max_length=60)
    last_name = models.CharField('Last Name', max_length=60)
    job = models.CharField('Job', max_length=1, choices=TYPE_JOBS)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'All employees'
        ordering = ['first_name']

    def __str__(self):
        return f"{self.id}-{self.first_name}-{self.last_name}"
