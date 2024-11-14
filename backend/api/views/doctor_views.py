from rest_framework import viewsets
from ..models import Doctor as DoctorModel
from ..serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializer
