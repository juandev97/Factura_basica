from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Persona, item, Factura
from django.http import HttpResponse, HttpResponseRedirect



#forms

from .forms import PersonaForm
from .forms import ItemForm
from .forms import FacturaForm

# Create your views here.

def inicio(request):
    	
	template = loader.get_template('index.html')
	contex = {
	
	}
	return HttpResponse(template.render(contex, request))


def get_facturas(request):
    facturas = Factura.objects.order_by('Fecha_E')
    template = loader.get_template('Lista_facturas.html')
    context= {

        'facturas' : facturas
    }
    return HttpResponse(template.render(context, request))




def new_persona(request):
    if(request.method == 'POST'):
        formP = PersonaForm(request.POST)
        if(formP.is_valid()):
            persona = formP.save(commit=False)
            persona.save()

            return HttpResponseRedirect('/home')
        else:
            print("Error Bad Data")
            return HttpResponseRedirect('/home')
    else:
        formP = PersonaForm(request.POST, request.FILES)
        template = loader.get_template('new_persona.html')
        context = {'form': formP
		}

        return HttpResponse(template.render(context, request))
        

def new_item(request):
    if request.method == 'POST':
        formI = ItemForm(request.POST)
        if formI.is_valid():
            Item = formI.save(commit=False)
            Item.save()
            return HttpResponseRedirect('/home')
        else:
            print("Error Bad Data")
            return HttpResponseRedirect('/home')
    else:
        formI = ItemForm(request.POST, request.FILES)
        template = loader.get_template('new_item.html')
        context = {'form': formI
        }
        return HttpResponse(template.render(context, request))
		



def new_factura(request):
    if request.method == 'POST':
        formF = FacturaForm(request.POST)
        if formF.is_valid():
            factura = formF.save(commit=False)
            factura.save()
            return HttpResponseRedirect('/home')
        else:
            print("Error Bad Data")
            return HttpResponseRedirect('/home')
    else:
        formF = FacturaForm(request.POST, request.FILES)
        template = loader.get_template('new_factura.html')
        context = {'form': formF
        }
        return HttpResponse(template.render(context, request))
		
