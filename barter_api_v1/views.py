from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.




@api_view(['GET'])
def get_category(request):
    categories = Category.objects.all()
    categories_serializer = CategorySerializer(categories, many=True)


    return Response(categories_serializer.data)

@api_view(['GET','POST'])
def save_category(request):

    return Response({})

@api_view(['GET'])
def get_product(request):
    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)
    return Response(products_serializer.data)

@api_view(['GET','POST'])
def save_product(requset):

    return Response({})
