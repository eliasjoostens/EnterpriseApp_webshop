from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
  type = models.CharField(max_length=255, null=True)
  name = models.CharField(max_length=255, null=True)
  introYear = models.IntegerField(null=True)
  price = models.FloatField(max_length=255, null=True)
  visible = models.BooleanField(default=False, null=True, blank=True)
  image = models.ImageField(null=True, blank=True)


