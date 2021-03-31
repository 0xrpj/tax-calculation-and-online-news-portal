from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 255)
    auth = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.auth)