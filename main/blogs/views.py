from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *


# Create Blog
@api_view(['POST'])
def create_blog(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all blogs.
@api_view(['GET'])
def get_blogs(request):
    try:
        blogs = BlogPost.objects.all()
        serializers = BlogListSerializer(blogs, many=True, context={'request': request})
        return Response(serializers.data)
    except BlogPost.DoesNotExist:
        return Response({"details": "Blog post not found"}, status=NotFound.status_code)
    

# Get a blog Details
@api_view(['GET'])
def get_blog(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)
        serializers = BlogPostSerializer(blog)
        return Response(serializers.data)

    except BlogPost.DoesNotExist:
        return Response({"details": "Blog post not found"}, status=NotFound.status_code)


@api_view(["PUT"])   
def update_blog(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)
        serializer = BlogPostSerializer(blog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return (serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except BlogPost.DoesNotExist:
        return Response({"details": "Blog post not found"}, status=NotFound.status_code)
    

@api_view(["DELETE"])
def delete_blog(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)
        blog.delete()
        return Response('Service was deleted')

    except BlogPost.DoesNotExist:
        return Response({"details": "Blog post not found"}, status=NotFound.status_code)
    

# Categories
@api_view(["GET"])
def get_categories(request):
    try:
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)
    
    except Category.DoesNotExist:
        return Response({"details": "No category!"}, status=NotFound.status_code)
    

 # Create Category
@api_view(["POST"])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# get category
@api_view(["GET"])
def get_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({"details": "No category!"}, status=NotFound.status_code)
    

# Update Category
@api_view(["PUT"])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    try:
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return (serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    except Category.DoesNotExist:
        return Response({"details": "Category Not Found!"}, status=NotFound.status_code)


# Delete Category
@api_view(['DELETE'])
def delete_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
        category.delete()
        return Response("Category has been deleted")
    
    except Category.DoesNotExist:
        return Response({"details": "Category Not Found!"}, status=NotFound.status_code)
    

# Get all Tags and Post new tag
@api_view(['GET', 'POST'])
def tag_list(request):
    # Get all tags and post new tag functions
    if request.method == "GET":
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Create Tag details with 3 methods get, put, delete
@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail(request, pk):
    try: 
        tag = Tag.objects.get(pk=pk)
        
    except Tag.DoesNotExist:
        return Response({"details": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Get a tag detail
    if request.method == "GET":
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update a tag
    elif request.method == "PUT":
        serializers = TagSerializer(tag, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        tag.delete()
        return Response("Tag is deleted!", status=status.HTTP_204_NO_CONTENT)

