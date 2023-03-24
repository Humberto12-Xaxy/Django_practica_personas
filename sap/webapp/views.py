from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona

# Create your views here.
def bienvenido(request):
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request= request, template_name='bienvenido.html', context= {'no_personas': no_personas, 'personas': personas})
