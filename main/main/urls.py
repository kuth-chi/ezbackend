
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls'))
]

# Rosetta URLs 
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta', include('rosetta.urls'))
    ]
