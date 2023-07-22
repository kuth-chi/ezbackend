from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.get_services, name="services"),
    path('services/create/', views.create_service, name="create_service"),
    path('services/<str:slug>/', views.get_service, name="service"),
    path('services/<str:slug>/update/', views.update_service, name="update_service"),
    path('services/<str:slug>/delete/', views.delete_service, name="delete_service"),
]
