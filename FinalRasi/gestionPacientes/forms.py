from django import forms
from .models import Paciente, HistoriaClinica

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento']

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'notas']
