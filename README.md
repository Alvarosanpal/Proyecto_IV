[![Build Status](https://travis-ci.org/Alvarosanpal/Proyecto_IV.svg?branch=master)](https://travis-ci.org/Alvarosanpal/Proyecto_IV)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://intense-mountain-50469.herokuapp.com/portada)

# Proyecto_IV
Repositorio para el proyecto de la asignatura "Infraestructura Virtual 18/19"

## Descripción
El proyecto tratará sobre un micro-servicio web que facilite el trámite de alquilar un equipo para prácticar algún deporte en Sierra Nevada y que de ciertos consejos sobre la altura del equipo y que muestre un precio estimado del alquiler.
Su funciomaniento consistirá en requerir unos datos (altura, peso, experiencia...) y como salida mostrar las sugerencias de equipos mas favorables respecto a los datos introducidos.

## Motivo de elección

He elegido este tema para el proyecto puesto que me encantan los deportes que se práctican en la sierra, y soy asiduo a practicarlos, por lo que he pensado que este proyecto podria facilitar mucho los trámites para alquiler de materiales.

## Herramientas

- El lenguaje de programación que se utilizará será [Python 3.6.0](https://www.python.org/). Pudiendo cambiar la versión puesto que trabajaremos en entornos virtuales con [virtualenv](https://virtualenv.pypa.io/en/stable/)
- Como framework utilizaré [Flask](http://flask.pocoo.org/), un micro-framework escrito en python.
- Como BD utilizaremos [MongoBD](https://www.mongodb.com/es)(Añadiré funcionalidad en un futuro próximo)
- Como editor de texto utilizaré Atom posiblemente.
- Para aplicar los test al proyecto y aplicar integracion continua utilizaré PyTest y [Travis](https://travis-ci.org/)

## Colaboración

En principio este proyecto será individual, pero está bastante relacionado con el proyecto de [vaderrama](https://github.com/vaderrama/Proyecto-IV) por lo que en un futuro podríamos acordar fusionar los micro-servicios, obteniendo un servicio mas completo y complejo.

## Funcionalidad y método de uso

Al acceder se mostrará un formulario, en el que se solicitarán distintos datos de usuario, tras introducirlos los utilizará para calcular la altura de la tabla, o de los esquis, según se haya seleccionado, después mostrará una página con los datos introducidos y a continuación mostrará las recomendaciones de altura del equipo, así como un precio estimado y algunos enlaces para proceder con su alquiler.

Despliegue: https://intense-mountain-50469.herokuapp.com/portada

# Fin Documentación
