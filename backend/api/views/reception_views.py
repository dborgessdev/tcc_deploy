from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Reception as ReceptionModel
from ..serializers import ReceptionSerializer

@api_view(['GET', 'POST'])
def receptionlist(request):
    receptions = ReceptionModel.objects.all()
    serialized_receptions = ReceptionSerializer(receptions, many=True)

    return Response(serialized_receptions.data, status=status.HTTP_200_OK)