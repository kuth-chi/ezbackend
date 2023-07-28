from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllUrls, name='all_urls')
]
