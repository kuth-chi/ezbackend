from rest_framework import serializers
from .models import Service, ServiceImage, ServicePrice


# Image Serializer
class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ServiceImage
        fields = ('id', 'image')

# Service Price Serializer
class ServicePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = '__all__'

# Service Serializer
class ServicesSerializer(serializers.ModelSerializer):
    # images = ServiceImageSerializer(many=True, read_only=True) # Many=True for OneToMany fields
    # service_price = ServicePriceSerializer(read_only=True) # OneToOne Relationship no need "many=True" and this method get all fields
    price = serializers.DecimalField(source='service_price.price', max_digits=9, decimal_places=2, read_only=True) # this method get custom field
    currency = serializers.CharField(source='service_price.currency', max_length=3, read_only=True) # this method get custom field
    
    
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'url', 'logo', 'slug', 'price', 'currency')
        # fields = ('id', 'description', 'url', 'logo', 'slug', 'price', 'images')

class ServiceDetailSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True, read_only=True)
    service_price = ServicePriceSerializer(read_only=True)
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'url', 'logo', 'slug', 'service_price', 'images')