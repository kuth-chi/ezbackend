from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('newsroom/', views.get_blogs, name='newsrooms'),
    path('newsroom/create/', views.create_blog, name='blog'),
    path('newsroom/<str:slug>/update/', views.update_blog, name='blog'),
    path('newsroom/<str:slug>/delete/', views.delete_blog, name='blog'),
    path('newsroom/<str:slug>/', views.get_blog, name='blog'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/', views.get_categories, name='categories'),
    path('categories/<str:pk>/', views.get_category, name='category'),
    path('categories/<str:pk>/update/', views.update_category, name='update_category'),
    path('categories/<str:pk>/delete/', views.delete_category, name='delete_category'),
    path('tags/<str:pk>/', views.tag_detail, name="tag_detail"),
    path('tags/', views.tag_list, name="tag_list"),
]

# URL for API_Views Decorator Multi-method views
urlpatterns = format_suffix_patterns(urlpatterns)
