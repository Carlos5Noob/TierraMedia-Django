"""
URL configuration for tierramedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # el path donde van las urls de la api
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include("app.urls")), # el path donde se incluyen las urls de la aplicación
    path('tierramedia/', include("django.contrib.auth.urls")), # el path donde se incluyen las urls de autenticación
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
