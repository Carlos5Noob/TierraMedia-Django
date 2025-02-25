from rest_framework import serializers
from app.models import Personaje  # Importa el modelo correcto

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'
