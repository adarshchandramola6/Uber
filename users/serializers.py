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


