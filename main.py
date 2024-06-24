import os
from tabulate import tabulate
import requests
from datetime import date


def iniciar():
    os.system('cls')
    while True:
        print("Bienvenido al sistema de gestión de citas medicas")
        print("1. Registrar una cita medica")
        print("2. Ver citas medicas")
        print("3. Una cita medica de hoy")
        print("4. Modificar estado de cita")
        print("5. Eliminar una cita medica")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            buscar_cita()
        elif opcion == "4":
            modificar_estado()
        elif opcion == "5":    
            eliminar_cita()
        elif opcion == "6":
            break 

def registrar_cita():
    os.system('cls')
    paciente = input("Ingrese el nombre del paciente: ")
    detalle = input("Ingrese el detalle de la cita: ")
    dia = input("Ingrese el día de la cita: ")
    hora = input("Ingrese la hora de la cita: ")
    data = {'paciente': paciente, 'detalle': detalle, 'dia': dia, 'hora': hora, 'estado': 'Agendada'}
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/registrar', data=data)
    print(respuesta.text)

    
def ver_citas():
    os.system('cls')
    respuesta = requests.get(url='http://localhost:3000/citas-medicas/todas')
    datos = []
    for dato in respuesta.json():
        temporal = []
        for key, value in dato.items():
            temporal.append(value)
        datos.append(temporal)
    headers = ['ID', 'Paciente', 'Detalle', 'Día', 'Hora', 'Estado']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)        

def buscar_cita():
    dia = date.today()
    respuesta = requests.get(url='http://localhost:3000/citas-medicas/buscar', data={'dia': dia})
    datos = []
    for dato in respuesta.json():
        temporal = []
        for key, value in dato.items():
            temporal.append(value)
        datos.append(temporal)
    headers = ['ID', 'Paciente', 'Detalle', 'Día', 'Hora', 'Estado']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def modificar_estado():
    id = input("Ingrese el ID de la cita medica: ")
    estado = input("Ingrese el estado de la cita medica: \n1. Agendado\n2. Atendida/o\n")
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/modificar/'+id, data={'estado': estado})
    print(respuesta.text)    

def eliminar_cita():
    id = input("Ingrese el ID de la cita medica: ")
    respuesta = requests.post (url='http://localhost:3000/citas-medicas/eliminar/'+id)
    print(respuesta.text)


iniciar()                                  