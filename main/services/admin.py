from django.contrib import admin
from .models import Service, ServicePrice, ServiceImage

# Register your models here.
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(ServiceImage)
