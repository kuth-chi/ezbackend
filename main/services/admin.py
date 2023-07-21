from django.contrib import admin
from .models import Service, ServicePrice, ServiceImage

# Admin inline Class methods
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage

# Admin inline Class methods of Image Model
class ServicePriceInline(admin.TabularInline):
    model = ServicePrice

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_price', 'created_at', 'edited_at')
    inlines = [ServicePriceInline, ServiceImageInline]


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicePrice)
admin.site.register(ServiceImage)
