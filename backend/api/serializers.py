from rest_framework import serializers
from .models import Pacient

class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacient
        fields = '__all__'
