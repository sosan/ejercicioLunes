import os
from flask import Flask, request, abort, render_template
import forms

app = Flask(__name__)


# app.config["SECRET_KEY"] = os.usrandom(12)


@app.route("/", methods=["GET", "POS"])
def home():
    contactar = forms.formularioContactar()

    # dentro del html ya podemos utilizar formilarios en lfask

    return render_template("usuario.html", form=contactar)


"""
@app.route("/parametros")
# http://127.0.0.1:5000/parametros?parametro=23
def param():
    param = request.args.get("parametro", "No hay parametro")
    return ("El parametro enviado {}".format(param))
"""


@app.route("/parametros")
@app.route("/parametros/<otraruta>")
@app.route("/parametros/<otraruta>/<int:entero>")
def param(otraruta="", entero=0):
    # si no hay entero salta el error 404
    return ("El parametro enviado {0} {1}".format(otraruta, entero))


@app.route("/usuarios/nombre")
def parame(nombre=""):
    return render_template("usuario.html", usuario=nombre)


@app.errorhandler(404)
def customerror404():
    pass


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run("127.0.0.1", 5000, debug=True)
