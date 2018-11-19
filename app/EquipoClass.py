from flask import Flask

class Equipo:

	def calcularAlturaTabla(altura , peso):
		if (altura - peso) >= 0:
			alturaT = altura * 0.85
		if (altura - peso) <= 0:
			alturaT = altura * 0.88
		return alturaT

	def calcularAlturaEsquis(altura , habilidad):
		if habilidad == "principiante":
			alturaE = altura - 18
		if habilidad == "medio":
			alturaE = altura - 14
		if habilidad == "experto":
			alturaE = altura - 10
		return alturaE

	def calcularPrecio (equipo):
		if equipo == 0:
			precio = 15
		if equipo == 1:
			precio = 15
		if equipo == 2:
			precio = 20
		if equipo == 3:
			precio = 25
		if equipo == 4:
			precio = 40
		return precio
