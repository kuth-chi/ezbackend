from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(Product)
admin.site.register(ProductImageGallery)
admin.site.register(ProductPrice)
admin.site.register(ProductDiscount)


