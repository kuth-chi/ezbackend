from .models import BlogPost, Tag, Category
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _ 


# Tags Serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        managed = True
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# Get blog list
class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'thumbnail', 'subtitle', 'authors', 'slug')


# Blog Post Serializer
class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'subtitle', 'header_image', 'thumbnail', 'content', 'tags', 'categories', 'created_at', 'updated_at', 'authors', 'editor', 'slug')
        
