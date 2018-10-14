from flask import Flask

app = Flask(__name__)

class Equipo:

	def __init__(self , equip , numero , exp):
		self.equipo = equip
		self.numeroPie = numero
		self.experiencia = exp

	def getEquipo():
		return equipo

	def getNumero():
		return numeroPie

	def getExp():
		return experiencia

	def setEquipo(equip):
		if (equip == "Snow" || equip == "Ski")
			equipo = equip
		else
			print ("No ha seleccionado un equipo correcto.")


	def setNumero(numero):
		numeroPie = numero

	def setExp(exp):
		experiencia = exp
