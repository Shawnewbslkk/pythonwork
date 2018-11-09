from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    #unknown
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ('uid', 'email', 'phone')

    uid = models.IntegerField(primary_key=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username