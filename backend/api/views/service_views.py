from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Service as ServiceModel
from ..serializers import ServiceSerializer

@api_view(['GET', 'POST'])
def servicelist(request):
    services = ServiceModel.objects.all()
    serialized_services = ServiceSerializer(services, many=True)

    return Response(serialized_services.data, status=status.HTTP_200_OK)

