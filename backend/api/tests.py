import logging
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Pacient, Doctor, Queue, Reception, Service, Nurse
from datetime import date
from django.utils import timezone

# Configuração do logger para exibir mensagens no console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Testes de Rotas da API
class ApiRoutesTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_pacients_route(self):
        url = reverse('pacient-list')  # Atualizado para usar o nome correto da rota
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'pacients' concluído com sucesso.")

    def test_list_doctors_route(self):
        url = reverse('doctor-list')  # Atualizado para usar o nome correto da rota
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'doctors' concluído com sucesso.")

    def test_list_queues_route(self):
        url = reverse('queue-list')  # Atualizado para usar o nome correto da rota
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'queues' concluído com sucesso.")

    def test_list_receptions_route(self):
        url = reverse('reception-list')  # Atualizado para usar o nome correto da rota
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'receptions' concluído com sucesso.")

    def test_list_services_route(self):
        url = reverse('service-list')  # Atualizado para usar o nome correto da rota
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'services' concluído com sucesso.")

    def test_list_nurses_route(self):
        url = reverse('nurse-list')  # Teste para a rota de enfermeiros
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'nurses' concluído com sucesso.")

# Testes dos Modelos e Banco de Dados
class ModelTests(TestCase):
    def setUp(self):
        self.pacient = Pacient.objects.create(
            name="João da Silva",
            cpf="12345678901",
            birth_date=date(1990, 1, 1)
        )
        
        self.doctor = Doctor.objects.create(
            name="Dra. Maria",
            specialty="Cardiologia"
        )
        
        self.nurse = Nurse.objects.create(
            name="Enfermeira Ana",
            registration_number="ENF123"
        )

    def test_create_pacient(self):
        pacient = Pacient.objects.get(cpf="12345678901")
        self.assertEqual(pacient.name, "João da Silva")
        self.assertEqual(pacient.birth_date, date(1990, 1, 1))
        logger.info("Teste de criação de 'Pacient' concluído com sucesso.")

    def test_create_doctor(self):
        doctor = Doctor.objects.get(name="Dra. Maria")
        self.assertEqual(doctor.specialty, "Cardiologia")
        logger.info("Teste de criação de 'Doctor' concluído com sucesso.")

    def test_create_nurse(self):
        nurse = Nurse.objects.get(registration_number="ENF123")
        self.assertEqual(nurse.name, "Enfermeira Ana")
        self.assertEqual(nurse.registration_number, "ENF123")
        logger.info("Teste de criação de 'Nurse' concluído com sucesso.")

    def test_create_queue(self):
        queue = Queue.objects.create(
            pacient=self.pacient,
            doctor=self.doctor,
            ticket="A001",
            priority=1,
            status='triagem',
            triage_nurse=self.nurse
        )
        self.assertEqual(queue.pacient.name, "João da Silva")
        self.assertEqual(queue.doctor.name, "Dra. Maria")
        self.assertEqual(queue.ticket, "A001")
        self.assertEqual(queue.priority, 1)
        self.assertEqual(queue.status, 'triagem')
        self.assertEqual(queue.triage_nurse.name, "Enfermeira Ana")
        logger.info("Teste de criação de 'Queue' concluído com sucesso.")

    def test_create_reception(self):
        reception = Reception.objects.create(
            pacient=self.pacient,
            nurse=self.nurse,
            description="Paciente com sintomas leves"
        )
        self.assertEqual(reception.pacient.name, "João da Silva")
        self.assertEqual(reception.nurse.name, "Enfermeira Ana")
        self.assertEqual(reception.description, "Paciente com sintomas leves")
        logger.info("Teste de criação de 'Reception' concluído com sucesso.")

    def test_create_service(self):
        # Criando paciente e médico com todos os campos obrigatórios
        pacient_instance = Pacient.objects.create(
            name="Paciente Teste",
            birth_date=timezone.now()  # Agora fornecemos uma data para o campo 'birth_date'
        )
        doctor_instance = Doctor.objects.create(name="Médico Teste")
        
        # Criando a instância de Service
        service = Service.objects.create(
            pacient=pacient_instance,
            doctor=doctor_instance,
            start_time=timezone.now(),
            final_status='alta',  # ou outro valor válido de 'final_status'
            observations="Test Service"
        )
        
        # Verificando se o objeto foi criado corretamente
        self.assertEqual(service.pacient.name, "Paciente Teste")
        self.assertEqual(service.doctor.name, "Médico Teste")
        self.assertEqual(service.final_status, 'alta')
        self.assertEqual(service.observations, "Test Service")
