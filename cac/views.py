from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando se accede por GET'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    parameters_get = request.GET.get('otro')
    return HttpResponse(f"""
        <h1>{titulo}</h1>
        <p>{parameters_get}</p>
    """)


def quienes_somos(request):
    #return redirect('saludar_por_defecto')
    return redirect(reverse('saludar', kwargs={'nombre':'Juliana'}))
    

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')

def saludar(request,nombre='Pepe'):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
        <p>Estoy haciendo mi primera prueba</p>
    """)

def ver_proyectos(request,anio,mes=1):
    return HttpResponse(f"""
        <h1>Proyectos del  - {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)

def ver_proyectos_2022_07(request):
    return HttpResponse(f"""
        <h1>Proyectos del mes 7 del año 2022</h1>
        <p>Listado de proyectos</p>
    """)

def ver_proyectos_anio(request,anio):
    return HttpResponse(f"""
        <h1>Proyectos del  {anio}</h1>
        <p>Listado de proyectos</p>
    """)

def cursos_detalle(request,nombre_curso):
    return HttpResponse(f"""
        <h1>{nombre_curso}</h1>
    """)


def cursos(request,nombre):
    return HttpResponse(f"""
        <h2>{nombre}</h2>
    """)