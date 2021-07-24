from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField('Name', max_length=50)
    short_name = models.CharField('Short Name', max_length=20)
    is_active = models.BooleanField('Active', default=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'All Departments'
        ordering = ['name']

    def __str__(self):
        return f"{self.id} - {self.name} - {self.short_name}"
