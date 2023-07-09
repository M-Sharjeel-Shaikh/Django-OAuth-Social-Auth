from django.contrib import admin
from django.urls import path, include
from GoogleAuth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GoogleAuth.urls')),
    path('accounts/', include('allauth.urls')),
]
