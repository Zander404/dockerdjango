from django.shortcuts import render
from banco.models import Banco
from banco.serializers import BancoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

# Create your views here.


#GET
@api_view(['GET'])
def bancoList(request):
    Banco = Banco.objects.all()
    serializer = BancoSerializer(Banco, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def bancoPost(request):
     serializer = BancoSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def bancoPut(request, pk):
    banco = Banco.objects.get(id=pk)
    serializer = BancoSerializer(banco, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def bancoDelete(request,pk):
    banco = Banco.objects.get(id=pk)
    banco.delete()
    return(Response('apagado'))         