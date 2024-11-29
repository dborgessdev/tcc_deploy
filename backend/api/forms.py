from django import forms
from .models import Pacient, Doctor, Nurse, Queue, Reception, Consultation

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

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = [
            'priority', 
            'main_complaint', 
            'disease_onset', 
            'physical_condition', 
            'medications', 
            'allergies', 
            'addictions', 
            'blood_pressure',
            'temperature',
            'oxygen_saturation',
            'heart_rate',
            'pain_scale',
            'glasgow_scale'
        ]

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = [
            'pacient',
            'doctor',
            'date',
            'observations'
        ]