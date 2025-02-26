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

    def get_personaje_estadisticas(self, request, pk):
        try:
            personaje = Personaje.objects.get(pk=pk)

            # Calculamos el ratio de victorias
            total_batallas = personaje.victorias + personaje.derrotas
            if total_batallas > 0:
                ratio_victorias = personaje.victorias / total_batallas
            else:
                ratio_victorias = 0

            # Obtenemos el arma, la facción y la ubicación
            arma = personaje.arma.nombre
            faccion = personaje.faccion.nombre
            ubicacion = personaje.ubicacion.nombre

            # Creamos una respuesta con las estadísticas
            estadisticas = {
                'nombre': personaje.nombre,
                'salud': personaje.salud,
                'mana': personaje.mana,
                'victorias': personaje.victorias,
                'derrotas': personaje.derrotas,
                'arma': arma,
                'faccion': faccion,
                'ubicacion': ubicacion,
                'foto': personaje.foto.url if personaje.foto else None,
                'ratio_victorias': round(ratio_victorias * 100, 2)
            }

            return Response(estadisticas)
        except Personaje.DoesNotExist:
            return Response({'error': 'Personaje no encontrado'}, status=404)

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
            'personajes': request.build_absolute_uri(reverse('api:personaje-list', request=request)),
            'armas': request.build_absolute_uri(reverse('api:arma-list', request=request)),
            'facciones': request.build_absolute_uri(reverse('api:faccion-list', request=request)),
            'ubicaciones': request.build_absolute_uri(reverse('api:ubicacion-list', request=request))
        })