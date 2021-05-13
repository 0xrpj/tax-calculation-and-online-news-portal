
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="loginapp\static\Images")
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='Politics')

    def __str__(self):
        return self.title + ' | ' + str(self.auth)

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})


class Tax(models.Model):
    monthly_salary = models.IntegerField(null=True)
    no_months = models.IntegerField(null=True)
    bonus = models.IntegerField(null=True)
    allowance = models.IntegerField(null=True)
    emp_provident = models.IntegerField(null=True)
    CIT = models.IntegerField(null=True)
    insurance = models.IntegerField(null=True)


class History(models.Model):
    taxable_income = models.IntegerField(null=True)
    annual_gross_salary = models.IntegerField(null=True)
    tax_slab_percentages = models.IntegerField(null=True)
    net_payable_tax = models.IntegerField(null=True)
