from django.urls import get_resolver
from django.shortcuts import render

def AllUrls(request):
    

    return render(request, "index.html")
