#contenido de test.py
import pytest
from app.app import calcularAlturaTabla , calcularAlturaEsquis , calcularPrecio

def test_alturaTabla():
	alturaTabla = calcularAlturaTabla(178,60)
	if alturaTabla > 0:
		pass

def test_alturaEsquis():
	alturaEsquis = calcularAlturaEsquis(178,medio)
	if alturaEsquis > 0:
		pass

def test_precio():
	precio = calcularPrecio(4)
	if precio > 0:
		pass
