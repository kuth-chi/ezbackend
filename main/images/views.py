from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from .models import Image
from .serializers import ImageSerializer

@api_view(['GET'])
def images_as_views(request):
    try:
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)  # You need to pass many=True for multiple objects
        return Response(serializer.data)
    except Image.DoesNotExist:
        return Response('No images', status=NotFound.status_code)
