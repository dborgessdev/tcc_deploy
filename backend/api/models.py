from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Base(models.Model):
    """Modelo base com campos comuns para outros modelos."""
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    disponivel = models.BooleanField("Disponível", default=True)

    class Meta:
        abstract = True


class Pacient(Base):
    """Modelo representando os pacientes."""
    name = models.CharField("Nome", max_length=255)
    cpf = models.CharField("CPF", max_length=11, unique=True)
    birth_date = models.DateField("Data de Nascimento")
    email = models.EmailField("E-mail", null=True, blank=True)
    photo = models.FileField(upload_to="images/", null=True, blank=True)
    phone_number = models.CharField("Número para Contato", max_length=20, null=True, blank=True)
    observations = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(Base):
    """Modelo representando os médicos."""
    name = models.CharField("Nome", max_length=255)
    crm = models.CharField("CRM", max_length=20, unique=True)
    specialty = models.CharField("Especialidade", max_length=255)

    def __str__(self):
        return self.name


class Nurse(Base):
    """Modelo representando os enfermeiros."""
    name = models.CharField("Nome", max_length=100)
    coren = models.CharField("COREN", max_length=20, unique=True)
    registration_number = models.CharField("Registro", max_length=100, null=True, blank=True)
    sector = models.CharField("Setor", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Queue(models.Model):

    # Prefixos
    PREFIX_MAP = {
        'pre_triagem': 'PTRI',
        'triagem': 'TRI',
        'pre_atendimento': 'PATEN',
        'em_atendimento': 'ATEN',
        'pos_atendimento': 'PSATE',
        'finalizado': 'ALT',
    }

    # Opções de status para o campo 'status'
    STATUS_CHOICES = [
        ('pre_triagem', 'Pré-triagem'),
        ('triagem', 'Triagem'),
        ('pre_atendimento', 'Pré-atendimento'),
        ('em_atendimento', 'Em Atendimento'),
        ('pos_atendimento', 'Pós-atendimento'),
        ('finalizado', 'Finalizado'),
    ]

    # Campos existentes
    pacient = models.ForeignKey('Pacient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    nurse = models.ForeignKey('Nurse', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pre_triagem')
    senha = models.CharField(max_length=20, blank=True, editable=False)
    priority = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    time_called = models.TimeField(null=True, blank=True)
    observations = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Permitir a atualização do paciente caso ele já esteja na fila
        if not self.pk and Queue.objects.filter(pacient=self.pacient).exclude(status='finalizado').exists():
            raise ValidationError(f"Paciente {self.pacient.name} já está em uma fila ativa!")

        # Geração da senha
        prefix = self.PREFIX_MAP.get(self.status, 'PTRI')
        if not self.senha:
            last_queue = Queue.objects.filter(senha__startswith=prefix).order_by('-id').first()
            next_number = int(last_queue.senha.split('-')[-1]) + 1 if last_queue else 1
            self.senha = f"{prefix}-{next_number:03}"
        else:
            number = self.senha.split('-')[-1]
            self.senha = f"{prefix}-{number}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.senha} - {self.pacient.name} - {self.status}"

    # Método para garantir que o status é válido (não é obrigatório, mas pode ajudar a evitar problemas)
    def clean(self):
        if self.status not in dict(self.STATUS_CHOICES):
            raise ValidationError(f"Status '{self.status}' não é um status válido.")



class Consultation(Base):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField("Data da Consulta", default=timezone.now)
    observations = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return f"Consulta de {self.pacient.name} com {self.doctor.name} em {self.date}"
    

class Reception(Base):
    """Modelo representando a recepção e o atendimento do paciente."""
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(
        'Nurse',  # Referência ao modelo Nurse
        on_delete=models.SET_NULL,
        null=True,  # Permitir valores nulos inicialmente
        blank=True  # Permitir o campo vazio nos formulários
    )
    reception_time = models.DateTimeField("Hora de Recepção", auto_now_add=True, null=True, blank=True)
    
    STATUS_CHOICES = [
        ('em_triagem', 'Em Triagem'),
        ('disponivel_para_atendimento', 'Disponível para Atendimento Médico'),
        ('em_atendimento', 'Em Atendimento'),
        ('finalizado', 'Finalizado'),
    ]
    status = models.CharField("Status", max_length=30, choices=STATUS_CHOICES, default='em_triagem')

    def __str__(self):
        return f"Recepção de {self.pacient.name} - Status: {self.status}"
