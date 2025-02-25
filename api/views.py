from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import Personaje
from .serializers import PersonajeSerializer

# ✅ Listar y crear personajes
class PersonajeListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        personajes = Personaje.objects.all()
        serializer = PersonajeSerializer(personajes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Obtener, actualizar y eliminar un personaje
class PersonajeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
