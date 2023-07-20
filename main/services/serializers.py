from rest_framework import serializers
from .models import Service, ServiceImage, ServicePrice


# Image Serializer
class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ServiceImage
        fields = ('id', 'image')

# Service Price Serializer
class ServicesPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = ('id', 'service_name', 'service_badge', 'price', 'currency', 'description')

# Service Serializer
class ServicesSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True, read_only=True)
    price = ServicesPriceSerializer(many=False, read_only=True)
    class Meta:
        model = Service
        fields = ('id', 'description', 'url', 'logo', 'slug', 'price', 'images')


