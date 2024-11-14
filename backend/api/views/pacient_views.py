from rest_framework import viewsets
from ..models import Pacient
from ..serializers import PacientSerializer

class PacientViewSet(viewsets.ModelViewSet):
    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer
