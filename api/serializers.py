from rest_framework import serializers
from movies.models import Movie
import base64
from django.core.files.base import ContentFile

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_image(self, value):
        if isinstance(value, str) and value.startswith('data:image'):
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen base64 no válida")
        return None
