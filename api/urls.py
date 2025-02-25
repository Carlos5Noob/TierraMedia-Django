from django.urls import path, include
from rest_framework import routers
from .views import PersonajeViewSet, ApiRootViewSet

router = routers.DefaultRouter()
router.register(r'personajes', PersonajeViewSet)
router.register(r'', ApiRootViewSet, basename='api-root')

urlpatterns = [
    path('', include(router.urls)),
]
