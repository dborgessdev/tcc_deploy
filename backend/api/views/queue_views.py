from rest_framework import viewsets
from ..models import Queue
from ..serializers import QueueSerializer

class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer
