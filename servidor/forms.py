from wtforms import Form, StringField, TextField, validators
from wtforms.fields.html5 import EmailField


class formularioContactar(Form):  # FlaskForm
    nombre = StringField("nombre:", validators=[
        validators.length(min=3, max=25, message="Nombre incorrecto")
    ])
    email = EmailField("email: ", validators=[
        validators.length(min=5, max=25)


    ])
    comentario = TextField("comentario")

# def formularioContactar():
#     formulario = TemplateFormLogin()
#     return formulario
