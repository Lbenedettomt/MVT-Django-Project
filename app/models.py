from django.db import models

# Create your models here.
class Register(models.Model):
    product = models.CharField(max_length=130)
    price = models.FloatField(max_length=100)