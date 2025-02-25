from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import Personaje, Arma, Faccion, Ubicacion
from .serializers import PersonajeSerializer, ArmaSerializer, FaccionSerializer, UbicacionSerializer


class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ArmaViewSet(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FaccionViewSet(viewsets.ModelViewSet):
    queryset = Faccion.objects.all()
    serializer_class = FaccionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiRootViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({
            'personajes': request.build_absolute_uri(reverse('personaje-list', request=request)),
            'armas': request.build_absolute_uri(reverse('arma-list', request=request)),
            'facciones': request.build_absolute_uri(reverse('faccion-list', request=request)),
            'ubicaciones': request.build_absolute_uri(reverse('ubicacion-list', request=request))
        })