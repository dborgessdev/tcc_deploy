from django import forms
from .models import Pacient, Doctor, Nurse, Queue

class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['name', 'birth_date', 'cpf', 'phone_number']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'crm', 'specialty']

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['disponivel', 'name', 'coren', 'sector']


class QueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ['pacient', 'nurse', 'priority', 'status']
