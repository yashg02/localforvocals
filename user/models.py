from django.db import models
from datetime import datetime

# Create your models here.
class channel(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20, default="")
    category = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='user/images', default="")
    password = models.CharField(max_length=100, default="pass1234", unique=False)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(max_length=100, null=True)
    date = models.DateField(default=datetime.now)

    objects=models.Manager()
    def __str__(self):
        return self.name
