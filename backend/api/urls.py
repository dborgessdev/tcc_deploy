# backend/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.pacient_views import PacientViewSet
from .views.doctor_views import DoctorViewSet
from .views.queue_views import QueueViewSet
from .views.reception_views import ReceptionViewSet
from .views.consultation_views import ConsultationViewSet
from .views.nurse_views import NurseViewSet
from .views.dashboard_views import dashboard_view
from .views.cadastro_views import (
    cadastrar_paciente, 
    cadastrar_medico, 
    cadastrar_enfermeiro, 
    cadastrar_atendimento
)

# Criação do roteador para os ViewSets
router = DefaultRouter()
router.register(r'pacients', PacientViewSet, basename='pacient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'queues', QueueViewSet, basename='queue')
router.register(r'receptions', ReceptionViewSet, basename='reception')
router.register(r'consultations', ConsultationViewSet, basename='consultation')
router.register(r'nurses', NurseViewSet, basename='nurse')

# URL patterns para a aplicação
urlpatterns = [
    # Inclui as URLs geradas pelo roteador sem prefixo extra
    path('', include(router.urls)),  # Alterado de 'api/' para '' para não repetir o 'api/'

    # Rotas específicas para a dashboard e cadastros via API
    path('cadastrar-paciente/', cadastrar_paciente, name='cadastrar_paciente'),
    path('cadastrar-medico/', cadastrar_medico, name='cadastrar_medico'),
    path('cadastrar-enfermeiro/', cadastrar_enfermeiro, name='cadastrar_enfermeiro'),
    path('cadastrar-atendimento/', cadastrar_atendimento, name='cadastrar_atendimento'),

    # Rota da dashboard
    path('dashboard/', dashboard_view, name='dashboard'),
]
