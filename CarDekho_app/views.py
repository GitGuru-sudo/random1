from django.shortcuts import render
from . models import carlist
from .api_file.serializers import CarSerlizers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests 
# Create your views here.
@api_view(['GET',"POST"])
def car_list_view(request):
    if request.method =="GET":
        car=carlist.objects.all()
        serializers=CarSerlizers(car,many=True)
        return Response(serializers.data)
    

    if request.method =="POST":
        serializers=CarSerlizers(data=request.data)
        if serializers.is_valid():
            return Response(serializers.data)
        
@api_view()
def car_detail_view(request,pk):
    car=carlist.objects.get(pk=pk)
    serlizers=CarSerlizers(car)
    return JsonResponse(serlizers.data)