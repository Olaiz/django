from django import forms
from apps.mascota.models import Mascota

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona

		fields = [
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]

		labels = {
			'nombre':'Nombre',
			'apellidos':'Apellidos',
			'edad':'Edad',
			'telefono':'Telefono',
			'email':'Email',
			'domicilio':'Domicilio',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'domicilio': forms.TextArea(attrs={'class':'form-control'}),
		}

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = Persona

		fields = [
			'numeros_mascotas',
			'razones',
		]

		labels = {
			'numeros_mascotas':'Num de mascotas',
			'razones':'Razones para adoptar',
		}
		widgets = {
			'numeros_mascotas': forms.TextInput(attrs={'class':'form-control'}),
			'razones': forms.TextArea(attrs={'class':'form-control'}),
		}