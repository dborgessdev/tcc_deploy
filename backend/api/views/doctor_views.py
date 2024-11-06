from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Doctor as DoctorModel
from ..serializers import DoctorSerializer

@api_view(['GET', 'POST'])
def doctorlist(request):
    doctors = DoctorModel.objects.all()
    serialized_doctors = DoctorSerializer(doctors, many =True)

    return Response(serialized_doctors.data, status=status.HTTP_200_OK)