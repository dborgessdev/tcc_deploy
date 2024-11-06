from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Pacient as PacientModel
from ..serializers import PacientSerializer

@api_view(['GET','POST'])
def pacientlist(request):
    pacients = PacientModel.objects.all()
    serialized_pacients = PacientSerializer(pacients, many=True)
    
    return Response(serialized_pacients.data, status=status.HTTP_200_OK)