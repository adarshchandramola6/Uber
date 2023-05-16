from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import*
from users.serializers import*

class GetStudentViews(APIView):

    def get(self,request):
     def post(self,request):
        params = request.data
        print("params",params)
        return Response("message","Done")
       
        print("req",request.get)
        name = request.data.get("first_name")
        print("name",name)
        if name:
            instance = Student.objects.filter(first_name)
        else:
            instance = Student.objects.all()
        instance = Student.objects.all()
        serializers = GetStudentSerializers(instance,many=True)
        return Response(serializers.data)
class GetOrdersViews(APIView):
   def get(self,orders):
      params = orders.data
      print("params",params)
      return Response("message","Done")

      print("sav",save.data)
      name = request.data.get(order_name)
      print("name",name)
      if name:
         instance = Student.objects.filter(first_name)
      else:
            instance = Orders.objects.all()
      instance = Orders.objects.all()
      serializers = GetOrdersSerializers(instance,many=True)
      return Response(serializers.data)   

















    



