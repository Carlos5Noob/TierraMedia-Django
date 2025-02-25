from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import Personaje
from .serializers import PersonajeSerializer

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiRootViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({
            'personajes': request.build_absolute_uri(reverse('personaje-list', request=request)),
        })