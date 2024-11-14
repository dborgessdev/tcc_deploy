from rest_framework import viewsets
from ..models import Nurse as NurseModel
from ..serializers import NurseSerializer

class NurseViewSet(viewsets.ModelViewSet):
    queryset = NurseModel.objects.all()
    serializer_class = NurseSerializer
