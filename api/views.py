from rest_framework import viewsets
from app.models import Personaje
from .serializers import MiModeloSerializer

class MiModeloViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = MiModeloSerializer