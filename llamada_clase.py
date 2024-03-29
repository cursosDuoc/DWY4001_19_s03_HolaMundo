#!/usr/bin/python3

# guardar en la carpeta del proyecto como "llamada_clase.py"

# del archivo Persona.py importa la clase Persona
from Persona import Persona

# ahora "el main" , que esta fuera de la clase.
perrin = Persona("Juan Eduardo Lopez", "12567864-2")
perrin.imprimir()

# En python, los atributos son publicos....
# y por tanto se pueden modificar directamente.
perrin.rut = "18752369-8"
perrin.imprimir()

# Las clases parten con Mayusculas y usan camel!
# mientras las funciones usan minusculas y se conectan con
# underscore
# ej clase (mal)  alumno_duoc -> (bien) AlumnoDuoc
# ej funcion (mal) imprimirDetalles -> (bien) imprimir_detalles

# Ej: crear una persona leyendo desde la consola:
nombre = input("Ingresa un nombre:")
rut = input("Ingresa el rut:")
personaIngresada = Persona(nombre, rut)
personaIngresada.imprimir()
