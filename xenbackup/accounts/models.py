from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    backup = models.CharField(max_length=100)


