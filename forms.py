from wtforms import Form
from wtforms import TextField, validators

class Formulario(Form):
    usuario = TextField ('Usuario', [validators.Required()] )
    contraseña = TextField ( 'Contraseña' , [validators.Required()] )


