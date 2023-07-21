from django.contrib import admin
from .models import Service, ServicePrice, ServiceImage

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_price', 'created_at', 'edited_at')

    def service_price(self, obj):
        return obj.serviceprice.price
    service_price_short_description = 'ServicePrice'

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicePrice)
admin.site.register(ServiceImage)
