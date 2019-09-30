#!/usr/bin/python3

# guardar como Persona.py en la carpeta del
# proyecto

# vamos a definir una clase. Primero una clase
# como las de Java.

class Persona:

	# en python hay un solo "constructor" , 
	# que se llama __init__ 
	# (doble underscore)init(doble underscore)
	# deben recibir un parametro self!!!
	# La gente en python se ha puedo de acuerdo para considerar
	# el si una variable parte con (underscore) _ se debe tratar
	# como si fuera privada
	def __init__(self, nombre, rut):
		self._nombre = nombre
		self.rut = rut

	def imprimir(self):
		texto = " ".join(("soy", self._nombre, "mi rut es", self.rut))
		print(texto)











