"""sicv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import *
from sicv import settings
from django.conf.urls.static import static
from django.views.decorators.clickjacking import xframe_options_exempt
from decorator_include import decorator_include

urlpatterns = [
    path('admin/', decorator_include(xframe_options_exempt, admin.site.urls) ),
    url(r'^explorer/', include('explorer.urls')),
    url(r'^', include('web.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
