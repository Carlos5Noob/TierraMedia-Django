from rest_framework import serializers
from app.models import Personaje  # Importa tus modelos

class MiModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'
