from django.db import models
from django.utils import timezone
import re


class Base(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    disponivel = models.BooleanField("Disponível", default=True)

    class Meta:
        abstract = True


class Pacient(Base):
    name = models.CharField("Nome", max_length=255)
    cpf = models.CharField("CPF", max_length=11, unique=True)
    birth_date = models.DateField("Data de Nascimento")
    email = models.EmailField("E-mail", null=True, blank=True)
    foto = models.FileField(upload_to="images/", null=True, blank=True)
    phone_number = models.CharField("Número para Contato", max_length=20, null=True, blank=True)
    observations = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(Base):
    name = models.CharField("Nome", max_length=255)
    crm = models.CharField("CRM", max_length=20, unique=True, default="000000")
    specialty = models.CharField("Especialidade", max_length=255)

    def __str__(self):
        return self.name


class Nurse(Base):
    disponivel = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    coren = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Queue(Base):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="queues")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, related_name="queues")
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, null=True, blank=True)
    ticket = models.CharField("Senha", max_length=10, unique=True)
    priority = models.IntegerField("Prioridade", default=0)
    called_at = models.DateTimeField("Horário de Chamada", null=True, blank=True)
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
        return (
            f"Senha: {self.ticket} - "
            f"Paciente: {self.pacient.name} - "
            f"Prioridade: {self.priority} - "
            f"Status: {self.get_status_display()}"
        )

    def save(self, *args, **kwargs):
        if not self.ticket:  # Gera o ticket automaticamente se não estiver definido
            # Tentando buscar o último ticket gerado
            last_ticket = Queue.objects.all().order_by('-id').first()

            if last_ticket and last_ticket.ticket:
                # Extrair número do ticket, assumindo que o formato seja "TICKET-001"
                match = re.search(r'(\d+)$', last_ticket.ticket)
                if match:
                    last_ticket_number = int(match.group(1))
                    new_ticket_number = last_ticket_number + 1
                else:
                    # Caso o ticket não tenha o formato esperado
                    new_ticket_number = 1
            else:
                # Caso não haja tickets no banco
                new_ticket_number = 1

            # Gerando um novo ticket no formato TICKET-001, TICKET-002, etc.
            self.ticket = f"TICKET-{new_ticket_number:03d}"

        super().save(*args, **kwargs)


class Reception(Base): 
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="receptions")
    queue = models.ForeignKey(
        Queue, on_delete=models.SET_NULL, null=True, blank=True, related_name="receptions"
    )
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, related_name="receptions", null=True, blank=True)
    data_reception = models.DateTimeField("Data de Triagem", auto_now_add=True)
    description = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return f'Triagem de {self.pacient.name} em {self.data_reception}'


class Consultation(Base):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="consultations", default=1)
    queue = models.ForeignKey(
        Queue, on_delete=models.SET_NULL, null=True, blank=True, related_name="consultations"
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="consultations", default=1)
    start_time = models.DateTimeField("Início do Atendimento", default=timezone.now)
    end_time = models.DateTimeField("Término do Atendimento", null=True, blank=True)
    status_choices = [
        ('alta', 'Alta'),
        ('enfermaria', 'Enfermaria'),
        ('internamento', 'Internamento')
    ]
    final_status = models.CharField("Status Final", max_length=20, choices=status_choices, null=True, blank=True)
    observations = models.TextField("Observações", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.end_time:
            self.on_service = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Atendimento de {self.pacient.name} iniciado em {self.start_time}"
