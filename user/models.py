from django.db import models
from datetime import datetime

# Create your models here.
class channel(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20, default="")
    category = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='user/images', default="")
    date = models.DateField(default=datetime.now)
    objects=models.Manager()
    def __str__(self):
        return self.name
