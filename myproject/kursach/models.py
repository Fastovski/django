from asyncio.windows_events import NULL
from django.db import models
from django.forms import IntegerField

# Create your models here.
#бд
      
class Supplier(models.Model):
    def __str__(self):
        return self.name
    name =  models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

class Products(models.Model):
    def __str__(self):
        return self.name
    name =  models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    cost = models.FloatField()
    number = models.IntegerField()
    mark = IntegerField(required=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=NULL)

class ExpertVoted(models.Model):
    user = models.CharField(max_length = 100)
    is_voted = models.BooleanField()

class ProductVote(models.Model):
    product1mark = models.IntegerField()
    product2mark = models.IntegerField()
    product3mark = models.IntegerField()
