from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse ("hola a todos desde django")

def saludo2(request):
    return HttpResponse ("hola desde mi segundo template")

def saluda_nombre(request, nombre):
    return HttpResponse(f"hola me llamo {nombre}!")

def nacimiento(request, edad):          #Desafio en que año naciste!!
    agno = datetime.now()
    a = agno.year - int(edad)
    return HttpResponse(f"naci en el año {a}!")

def probandoTemplate(self):

    nombre = "Facundo"
    apellido = "Aban"

    diccionario = {"nombre":nombre, "apellido":apellido}

    miHtml = open("E:\Python project\proyecto1\proyecto1\proyecto1\template\template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)



