import logging
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Pacient, Doctor, Queue, Reception, Service
from datetime import date

# Configuração do logger para exibir mensagens no console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Testes de Rotas da API
class ApiRoutesTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_pacients_route(self):
        url = reverse('list-pacients')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'list-pacients' concluído com sucesso.")

    def test_list_doctors_route(self):
        url = reverse('list-doctors')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'list-doctors' concluído com sucesso.")

    def test_list_queues_route(self):
        url = reverse('list-queues')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'list-queues' concluído com sucesso.")

    def test_list_receptions_route(self):
        url = reverse('list-receptions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'list-receptions' concluído com sucesso.")

    def test_list_services_route(self):
        url = reverse('listservice')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info("Teste de rota 'listservice' concluído com sucesso.")

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

    def test_create_pacient(self):
        pacient = Pacient.objects.get(cpf="12345678901")
        self.assertEqual(pacient.name, "João da Silva")
        self.assertEqual(pacient.birth_date, date(1990, 1, 1))
        logger.info("Teste de criação de 'Pacient' concluído com sucesso.")

    def test_create_doctor(self):
        doctor = Doctor.objects.get(name="Dra. Maria")
        self.assertEqual(doctor.specialty, "Cardiologia")
        logger.info("Teste de criação de 'Doctor' concluído com sucesso.")

    def test_create_queue(self):
        queue = Queue.objects.create(
            pacient=self.pacient,
            doctor=self.doctor,
            ticket="A001",
            prioridade=1
        )
        self.assertEqual(queue.pacient.name, "João da Silva")
        self.assertEqual(queue.doctor.name, "Dra. Maria")
        self.assertEqual(queue.ticket, "A001")
        self.assertEqual(queue.prioridade, 1)
        logger.info("Teste de criação de 'Queue' concluído com sucesso.")

    def test_create_reception(self):
        reception = Reception.objects.create(
            pacient=self.pacient,
            doctor=self.doctor,
            description="Paciente com sintomas leves"
        )
        self.assertEqual(reception.pacient.name, "João da Silva")
        self.assertEqual(reception.doctor.name, "Dra. Maria")
        self.assertEqual(reception.description, "Paciente com sintomas leves")
        logger.info("Teste de criação de 'Reception' concluído com sucesso.")

    def test_create_service(self):
        service = Service.objects.create(
            pacient=self.pacient,
            doctor=self.doctor,
            date_time_start="2024-11-13 10:00",
            descriptions="Consulta inicial"
        )
        self.assertEqual(service.pacient.name, "João da Silva")
        self.assertEqual(service.doctor.name, "Dra. Maria")
        self.assertEqual(service.date_time_start.strftime("%Y-%m-%d %H:%M"), "2024-11-13 10:00")
        self.assertEqual(service.descriptions, "Consulta inicial")
        logger.info("Teste de criação de 'Service' concluído com sucesso.")
