from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField


class TemplateFormLogin(Form):  # FlaskForm
    nombre = StringField("nombre:")
    email = EmailField("email: ")
    comentario = TextField("comentario")


# def formularioContactar():
#     formulario = TemplateFormLogin()
#     return formulario
