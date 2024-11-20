from django.shortcuts import render
from ..forms import PacientForm, DoctorForm, NurseForm, QueueForm
from ..models import Pacient, Nurse, Doctor

def cadastrar_paciente(request):
    if request.method == "POST":
        form = PacientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "cadastro_success.html")  # Página de sucesso
    else:
        form = PacientForm()

    return render(request, "cadastrar_paciente.html", {"form": form})

def cadastrar_medico(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)  # Usando o formulário correto para médico
        if form.is_valid():
            form.save()
            return render(request, "cadastro_success.html")  # Página de sucesso
    else:
        form = DoctorForm()

    return render(request, "cadastrar_medico.html", {"form": form})

def cadastrar_enfermeiro(request):
    if request.method == "POST":
        form = NurseForm(request.POST)  # Usando o formulário correto para enfermeiro
        if form.is_valid():
            form.save()
            return render(request, "cadastro_success.html")  # Página de sucesso
    else:
        form = NurseForm()

    return render(request, "cadastrar_enfermeiro.html", {"form": form})

def cadastrar_atendimento(request):
    if request.method == "POST":
        form = QueueForm(request.POST)  # Usando o formulário correto para atendimento
        if form.is_valid():
            form.save()
            return render(request, "cadastro_success.html")  # Página de sucesso
    else:
        form = QueueForm()

    return render(request, "cadastrar_atendimento.html", {"form": form})
