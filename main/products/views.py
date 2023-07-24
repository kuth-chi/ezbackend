from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status


# Function Create & Get all Categories
@api_view(["GET", "POST"])
def product_categories(request):
    # GET and POST
    if request.method == 'GET':	
        try:
            product_categories = ProductCategory.objects.all()
            serializers = ProductCategorySerializer(product_categories, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except ProductCategory.DoesNotExist:
            return Response("Product category not found", status=NotFound.status_code)
    
    elif request.method == 'POST':
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Function Update, Get, and Delete a Product category
@api_view(["GET", "PUT", "DELETE"])
def product_category_detail(request, pk):
    try:
        product_category = ProductCategory.objects.get(pk=pk)
    except ProductCategory.DoesNotExist:
        return Response("Product category not found", status=NotFound.status_code)

    # Get a product category
    if request.method == 'GET':
        serializer = ProductCategorySerializer(product_category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a product category
    elif request.method == 'PUT':
        serializer = ProductCategorySerializer(product_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a product category
    elif request.method == 'DELETE':
        product_category.delete()
        return Response("A product category is deleted", status=status.HTTP_204_NO_CONTENT)
    

# Function Product Tags 
@api_view(["GET", "POST"])
def product_tags(request):
    try:
        product_tags = ProductTag.objects.all()

    except ProductTag.DoesNotExist:
        return Response({"message": "Product Tag Not Exists"}, status=status.HTTP_404_NOT_FOUND)
    
    # Get all tags
    if request.method == 'GET':
        serializers = ProductTagSerializer(product_tags, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
        
    # Create a product tag
    elif request.method == "POST":
        serializers = ProductTagSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
    

@api_view(["GET", "PUT", "DELETE"])
def product_tag_detail(request, pk):
    try:
        product_tag = ProductTag.objects.get(pk=pk)
    
    except ProductTag.DoesNotExist:
        return Response({"message": "Product tag not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == "GET":
        serializer = ProductTagSerializer(product_tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ProductTagSerializer(product_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        product_tag.delete()
        return Response({"message": "A product tag has been deleted"}, status=status.HTTP_404_NOT_FOUND)


# Build Product API
@api_view(["GET", "POST"])
def products(request):
    try:
        products = Product.objects.all()

    except Product.DoesNotExist:
        return Response({"message": "No products were found"}, status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == "GET":
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
        
    elif request.method == "POST":
        serializers = ProductDetailsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=NotFound.status_code)
    
@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=NotFound.status_code)
    
    
    if request.method == "GET":
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = ProductDetailsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        product.delete()
        return Response({'message': 'Product is deleted'}, status=status.HTTP_404_NOT_FOUND)
    
