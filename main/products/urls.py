
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products-categories/', views.product_categories, name='product_categories'),
    path('products-categories/<str:pk>/', views.product_category_detail, name='product_category_detail'),
    path('products-tags/', views.product_tags, name='product_tags'),
    path('products-tags/<str:pk>/', views.product_tag_detail, name='product_tag_detail'),
    path('products/', views.products, name='products'),
    path('products/<str:slug>/', views.product_detail, name='product'),
]

urlpatterns += format_suffix_patterns(urlpatterns)