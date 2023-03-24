from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from personas.models import Persona
from personas.forms import PersonaForm

# Create your views here.
def detalle_personas(request, id):
    # persona = Persona.objects.get(pk= id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, template_name= 'personas/detalle.html', context= {'persona': persona})

# PersonaForm = modelform_factory(model= Persona, exclude= [])

def nueva_persona(request ):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:    
        formpersona= PersonaForm()
    
    return render(request, template_name= 'personas/nuevo.html', context= {'formaPersona': formpersona})

def editar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance= persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:    
        formpersona= PersonaForm(instance= persona)
    
    return render(request, template_name= 'personas/editar.html', context= {'formaPersona': formpersona})

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

    