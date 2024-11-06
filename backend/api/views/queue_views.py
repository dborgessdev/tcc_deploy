from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Queue as QueueModel
from ..serializers import QueueSerializer

@api_view(['GET','POST'])
def queuelist(request):
    queues = QueueModel.objects.all()
    serialized_queues = QueueSerializer(queues, many=True)
    
    return Response(serialized_queues.data, status=status.HTTP_200_OK)