from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views.pacient_views import PacientViewSet
from .views.doctor_views import DoctorViewSet
from .views.queue_views import QueueViewSet
from .views.reception_views import ReceptionViewSet
from .views.service_views import ServiceViewSet
from .views.nurse_views import NurseViewSet

# Cria um roteador para rotas padrão
router = DefaultRouter()
router.register(r'pacients', PacientViewSet, basename='pacient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'queues', QueueViewSet, basename='queue')
router.register(r'receptions', ReceptionViewSet, basename='reception')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'nurses', NurseViewSet, basename='nurse')

# Inclui as rotas do roteador
urlpatterns = [
    path('', include(router.urls)),
]
