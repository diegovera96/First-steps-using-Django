from dataclasses import dataclass
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request):
        return Response(data="Hello, World !", status=200)

# Create your views here.

class PersonAPIView(APIView):
    def get(self, request):
        return Response(data="Get APIView de Person", status=200)
    
    def patch(self, request):
        return Response(data="Patch APIView de Person", status=200)
    
    def delete(self, request):
        return Response(data="Delete APIView de Person", status=200)
    
    def post(self, request):
        return Response(data="Post APIView de Person", status=200)

class PetAPIView(APIView):
    def get(self, request):
        return Response(data="Get APIView de Pet", status=200)
    
    def patch(self, request):
        return Response(data="Patch APIView de Pet", status=200)
    
    def delete(self, request):
        return Response(data="Delete APIView de Pet", status=200)
    
    def post(self, request):
        return Response(data="Post APIView de Pet", status=200)