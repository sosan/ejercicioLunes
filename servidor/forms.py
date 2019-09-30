from wtforms import Form, StringField, TextField, validators, HiddenField
from wtforms.fields.html5 import EmailField


# crear una validacion propia
def honeyPot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError("El campo esta vacio")  # siginifca que es un robot


class formularioContactar(Form):  # FlaskForm
    nombre = StringField("nombre:", validators=[
        validators.required("Estas obligado a rellenar este campo"),
        validators.length(min=3, max=25, message="Nombre incorrecto")
    ])
    email = EmailField("email: ", validators=[
        validators.required("Este campo es requerido"),
        validators.email("Ingrese un email: ")

    ])
    comentario = TextField("comentario")

    # señuelo
    sunyuelo = HiddenField("", {honeyPot})

# def formularioContactar():
#     formulario = TemplateFormLogin()
#     return formulario
