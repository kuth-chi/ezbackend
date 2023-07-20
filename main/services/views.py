from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from .models import Service
from .serializers import ServicesSerializer


# Create your views here.
@api_view(['GET'])
def get_services(request):

    try:
        services = Service.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)
    except Service.DoesNotExist:
        return Response('Service not found', status=NotFound.status_code)
