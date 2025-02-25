from django.urls import path
from .views import ApiRootView, PersonajeListCreateAPIView, PersonajeDetailAPIView

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),  # Agregamos la API root aquí
    path('api/personajes/', PersonajeListCreateAPIView.as_view(), name='personaje-list-create'),
    path('api/personajes/<int:pk>/', PersonajeDetailAPIView.as_view(), name='personaje-detail'),
]