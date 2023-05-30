from rest_framework import serializers
from users.models import(Student,Orders)


class Student(serializers.ModelSerializer):
    class Meta:
        models=Student
        fields = '__all__'


class Orders(serializers.ModelSerializer):
    class Meta:
        models=Orders
        fields = '__all__'                


class StudentAddressSerializers(serializers.ModelSerializer):
    class Meta:
        models=Student
        fields = '__all__'                


class StudentDetailsAddressSerializers(serializers.ModelSerializer):
    addresses = StudentAddressSerializers(many=True)
    class Meta:
        models=Student
        fields = ("first_name","sur_name","birth","addresses")         

            