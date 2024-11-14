from django.db import models
from django.utils import timezone


# Classe Base com campos comuns
class Base(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    disponivel = models.BooleanField("Disponível", default=True)

    class Meta:
        abstract = True


# Modelo para Paciente
class Pacient(Base):
    name = models.CharField("Nome", max_length=255, null=False, blank=False)
    cpf = models.CharField("CPF", max_length=11, unique=True, null=False, blank=False)
    birth_date = models.DateField("Data de Nascimento", null=False, blank=False)
    foto = models.FileField(upload_to="images/", null=True, blank=True)
    phone_number = models.CharField("Número para Contato", max_length=20, null=True, blank=True)
    observations = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return self.name


# Modelo para Médico
class Doctor(Base):
    name = models.CharField("Nome", max_length=255, null=False, blank=False)
    specialty = models.CharField("Especialidade", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


# Modelo para Enfermeiro
class Nurse(Base):
    name = models.CharField("Nome", max_length=255, null=False, blank=False)
    registration_number = models.CharField("Número de Registro", max_length=20, unique=True)

    def __str__(self):
        return self.name


# Modelo de Atendimento com Status
class Queue(Base):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="queues")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="queues", null=True, blank=True)
    ticket = models.CharField("Senha", max_length=10, unique=True)
    priority = models.IntegerField("Prioridade", default=0)
    status_choices = [
        ('pre_triagem', 'Pré-triagem'),
        ('triagem', 'Triagem'),
        ('pre_atendimento', 'Pré-atendimento'),
        ('em_atendimento', 'Em Atendimento'),
        ('pos_atendimento', 'Pós-atendimento'),
        ('finalizado', 'Finalizado'),
    ]
    status = models.CharField("Status", max_length=20, choices=status_choices, default='pre_triagem')
    triage_nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, related_name="triages", null=True, blank=True)
    creation_date = models.DateTimeField("Data de Criação", auto_now_add=True)
    observations = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return f'Senha: {self.ticket} - Paciente: {self.pacient.name} - Status: {self.status}'


# Modelo de Triagem
class Reception(Base):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="receptions")
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, related_name="receptions", null=True, blank=True)
    data_reception = models.DateTimeField("Data de Triagem", auto_now_add=True)
    description = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return f'Triagem de {self.pacient.name} por {self.nurse.name if self.nurse else "Desconhecido"} em {self.data_reception}'


# Modelo de Serviço/Atendimento
class Service(Base):
        

    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="services")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="services")
    start_time = models.DateTimeField("Início do Atendimento", default=timezone.now)
    end_time = models.DateTimeField("Término do Atendimento", null=True, blank=True)
    status_choices = [
        ('alta', 'Alta'),
        ('enfermaria', 'Enfermaria'),
        ('internamento', 'Internamento')
    ]
    final_status = models.CharField("Status Final", max_length=20, choices=status_choices, null=True, blank=True)
    on_service = models.BooleanField("Em Atendimento", default=True)
    observations = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return f"Atendimento de {self.pacient} com {self.doctor} iniciado em {self.start_time}"
