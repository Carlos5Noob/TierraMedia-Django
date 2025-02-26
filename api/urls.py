from django.urls import path, include
from rest_framework import routers
from .views import PersonajeViewSet, ArmaViewSet, FaccionViewSet, UbicacionViewSet, ApiRootViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r'personajes', PersonajeViewSet)
router.register(r'armas', ArmaViewSet)
router.register(r'facciones', FaccionViewSet)
router.register(r'ubicaciones', UbicacionViewSet)
router.register(r'', ApiRootViewSet, basename='api-root')

urlpatterns = [
    path('', include(router.urls)),
        path('personaje/<int:pk>/estadisticas/', PersonajeViewSet.as_view({'get': 'get_personaje_estadisticas'}), name='personaje-estadisticas'),
]
