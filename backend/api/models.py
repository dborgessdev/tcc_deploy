from django.db import models
# Create your models here.

class Base(models.Model):
    # Define uma classe base chamada 'Base' que herda de 'models.Model'.
    # Essa classe será usada como um modelo abstrato, permitindo que outras classes herdem seus campos.
    
    created_at = models.DateTimeField("Criado", auto_now_add=True)
    # Cria um campo que armazena a data e hora de criação do registro.
    update_at = models.DateTimeField("Atualizado", auto_now=True)
    # Atualiza automaticamente a data e hora toda vez que o registro é salvo.
    disponivel = models.BooleanField("Status", default=True)

    class Meta:
        abstract = True
        # Define que esta classe é abstrata.
        # Isso significa que não será criada uma tabela correspondente para a classe Base no banco de dados,
        # mas suas propriedades poderão ser herdadas por outras classes que a utilizam.

########################################################################################################

class Pacient(Base):
    name = models.CharField("Nome", max_length=255, null=False, blank=False)
    cpf = models.CharField("CPF", max_length=11, unique=True, null=False, blank=False)
    birth_date = models.DateField("Data de Nascimento", null=False, blank=False)
    foto = models.FileField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.name
    
########################################################################################################

class Doctor(Base):
    name = models.CharField("Nome", max_length=255, null=False, blank=False)
    specialty = models.CharField("Especialidade", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

########################################################################################################

class Queue(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="queues")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="queues")
    ticket = models.CharField("Senha", max_length=10, unique=True)
    creation_date = models.DateTimeField("Data de Criação", auto_now_add=True)
    prioridade = models.IntegerField("Prioridade", default=0)

    def __str__(self):
        return f'Senha: {self.ticket} - Paciente: {self.pacient.name} - Médico: {self.doctor.name}'
    
########################################################################################################

class Screening(Base):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="screenings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="screenings")
    data_screening = models.DateTimeField("Data de Triagem", auto_now_add=True)
    description = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return f'Triagem de {self.pacient.name} por {self.doctor.name} em {self.data_screening}'
    
########################################################################################################

class Service(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="services")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="services")
    date_time_start = models.DateTimeField("Data e Hora de Início")  # Agora é editável
    date_time_end = models.DateTimeField("Data e Hora de Término", null=True, blank=True)
    on_service = models.BooleanField("Em Atendimento", default=True)
    descriptions = models.TextField("Observações", null=True, blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"Atendimento de {self.pacient} com {self.doctor} em {self.date_time_start}"
