from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dashboard')

class Post(models.Model):
    title = models.CharField(max_length = 255)
    auth = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=255, default='Politics')

    def __str__(self):
        return self.title + ' | ' + str(self.auth)
    
    def get_absolute_url(self):
        return reverse('dashboard' , kwargs={'pk': self.pk} )