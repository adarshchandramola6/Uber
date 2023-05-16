from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25,null=True,blank=True)
    sur_name = models.TextField(null=True,blank=True)
    birth = models.DateField(null=True,blank=True)
    mobile = models.IntegerField(max_length=10,null=True,blank=True)
    Gender_types = (
            (1,'male'),
            (2,'female'),
            (3,'other'),
    )
    gender = models.IntegerField(
        max_length=10,
        choices=Gender_types,
        default=1
    )
class Orders(models.Model):
    order_name = models.CharField(max_length=25,null=True,blank=True)
    order_price = models.IntegerField(null=True,blank=True)
    order_discount = models.IntegerField(null=True,blank=True)
    order_quantity = models.IntegerField(max_length=10,null=True,blank=True)
    

