"""
URL configuration for jamjam_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # include

### for Swagger API Docs
from rest_framework.permissions import AllowAny
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="jamjam-AI",
        default_version="v0",
        description="이제는 POSTMAN 안써도 돼 !",
    ),
    public=True,
    permission_classes=[AllowAny] # Swagger에는 인증 필요없도록 설정
) 

### url patterns
urlpatterns = [
    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # project
    path("admin/", admin.site.urls),
    path('user/', include('user.urls')), #user/urls.py
    path('flip_detection/', include('flip_detection.urls')), # flip_detection/urls.py
    path('sleep_detection/', include('sleep_detection.urls')), # sleep_detection/urls.py
]
