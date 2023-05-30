from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25,null=True,blank=True)
    sur_name = models.TextField(null=True,blank=True)
    birth = models.DateField(null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.first_name)
    Gender_types = (
            (1,'male'),
            (2,'female'),
            (3,'other'),
    )
    gender = models.IntegerField(
        choices=Gender_types,
        default=1
    )
class Orders(models.Model):
    order_name = models.CharField(max_length=25,null=True,blank=True)
    order_price = models.IntegerField(null=True,blank=True)
    order_discount = models.IntegerField(null=True,blank=True)
    order_quantity = models.IntegerField(null=True,blank=True)

class StudentAddress(models.Model):
    student = models.ForeignKey(Student,on_delete =models.CASCADE,null=True,related_name="addresses")
    street_name = models.CharField(max_length=25,null=True,blank=True)
    house_number = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=25,null=True,blank=True)
    state= models.CharField(max_length=10,null=True,blank=True)
    pincode= models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.street_name)
  

