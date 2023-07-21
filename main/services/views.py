from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Service
from .serializers import ServiceDetailSerializer, ServicesSerializer


# Get all services.
@api_view(['GET'])
def get_services(request):

    try:
        services = Service.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)
    except Service.DoesNotExist:
        return Response('Service not found', status=NotFound.status_code)


# Get a service
@api_view(['GET'])
def get_service(request, slug):
    service = Service.objects.get(slug=slug)
    serializer = ServiceDetailSerializer(service, many=False)
    return Response(serializer.data)


# Update service
@api_view(['PUT'])
def update_service(request, slug):
    try:
        service = Service.objects.get(slug=slug)

        # Create the serializer with the existing service instance and data from the request
        serializer = ServiceDetailSerializer(service, data=request.data)

        # Validate the data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Service.DoesNotExist:
        return Response({'detail': 'Service not found.'}, status=status.HTTP_404_NOT_FOUND)
    

# Delete Service Data
@api_view(['DELETE'])
def delete_service(request, slug):
    service = Service.objects.get(slug=slug)
    service.delete()
    return Response('Service was deleted')
