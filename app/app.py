from flask import Flask, render_template
from flask import request , redirect, url_for

app = Flask(__name__)

@app.route('/')                        
def hello_world():                      
    return render_template('bienvenido.html')

@app.route('/user/', methods=['GET','POST'])
@app.route('/user/<user>', methods=['GET','POST'])
def user(user=None , psw=None):
	if request.method == 'POST':
		parametro1 = request.form['username']
		parametro2 = request.form['password']		
		return redirect(url_for('user', user=parametro1 , psw=parametro2))
	return render_template('user.html', usuario = user , clave = psw)

@app.route('/busqueda' , methods=['GET'])
def busqueda():
	return render_template('busqueda.html')

@app.route('/resultado' , methods=['POST'])
def resultado(deporte = None , altura = None , peso = None , habilidad = None , equipo = None):
	deporte = request.form['deporte']
	altura = request.form['altura']
	peso = request.form['peso']
	habilidad = request.form['habilidad']
	equipo = request.form['equipo']
	alturaT = calcularAlturaTabla(int(altura) , int(peso))
	alturaE = calcularAlturaEsquis(int(altura) , habilidad)
	precio = calcularPrecio(int(equipo))
	return render_template('resultado.html' , deporte = deporte , altura = altura, peso = peso ,habilidad =habilidad, equipo = equipo , alturaT = alturaT , alturaE = alturaE , precio = precio)


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


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', err = error)
