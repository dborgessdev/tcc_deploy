from rest_framework import viewsets
from ..models import Reception
from ..serializers import ReceptionSerializer

class ReceptionViewSet(viewsets.ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
