from django.shortcuts import render
from django.http import JsonResponse
from .models import Articel
from .serializers import ArticelSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def articel_list(request, format=None):

    if request.method == 'GET' :
        articels = Articel.objects.all()
        serialize_aricel = ArticelSerializer(articels, many = True)
        return Response(serialize_aricel.data)
    if request.method == 'POST':
        serialize_aricel = ArticelSerializer(data=request.data)
        if serialize_aricel.is_valid():
            serialize_aricel.save()
            return Response(serialize_aricel.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def detail_articel(request, id, format=None):
    try:
        detail_articel = Articel.objects.get(pk=id)
    except Articel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    

    if request.method == "GET":
        serializer =ArticelSerializer(detail_articel)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ArticelSerializer(detail_articel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        detail_articel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
