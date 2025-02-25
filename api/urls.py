from django.urls import path
from .views import PersonajeListCreateAPIView, PersonajeDetailAPIView

urlpatterns = [
    path('api/personajes/', PersonajeListCreateAPIView.as_view(), name='personaje-list-create'),
    path('api/personajes/<int:pk>/', PersonajeDetailAPIView.as_view(), name='personaje-detail'),
]
