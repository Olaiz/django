from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.adopcion.models import Persona, Solicitud
# Create your views here.

def index_adopcion(request):
	return HttpResponse("Soy la pagina de adopcion")

class SolicitudList(ListView):
	model= Solicitud
	template_name = 'adopcion/solicitud_list.html'