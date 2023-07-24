from .models import ProductCategory, ProductTag, Product, ProductImageGallery, ProductPrice, ProductDiscount
from rest_framework import serializers



# Product categories Serializer
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'parent_category', 'slug')


# Product tags Serializer
class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        managed = True
        fields = ('id', 'name', 'slug')



# Product Image Gallery Serializer
class ProductImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageGallery
        fields = "__all__"


#  Product Price Serializer
class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = "__all__"


# Product Discount Serializer
class ProductDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDiscount
        fields = "__all__"


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    product_price = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ('title', 'description', 'product_price', 'logo', 'thumb', 'slug',)

    def get_product_price(self, obj):
        try:
            return ProductPrice.get(product=obj).base_price
        except ProductPrice.DoesNotExist:
            return None


# Product Details Serializer
class ProductDetailsSerializer(serializers.ModelSerializer):
    images = ProductImageGallerySerializer(source='product_images_gallery', many=True, read_only=True)
    price = ProductPriceSerializer(source='product_price', read_only=True)
    discount = ProductDiscountSerializer(source='product_discount', many=True, read_only=True)
    
    # Nest serializer objects method
    tag = ProductTagSerializer(many=True, read_only=True)
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ('title', 'description', 'logo', 'header', 'thumb', 'images', 'price', 'discount', 'url', 'created_date', 'updated_date', 'slug', 'tag', 'category')
