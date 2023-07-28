from flask import Flask, render_template, url_for
import requests
import json
import datetime
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    now = datetime.datetime.now()
    rp = requests.get("http://127.0.0.1:81/api/personas/",
            auth=(usuario, clave))
    cant_personas = json.loads(rp.content)['count']
    rb = requests.get("http://127.0.0.1:81/api/barrios/",
            auth=(usuario, clave))
    cant_barrios = json.loads(rb.content)['count']
    rc = requests.get("http://127.0.0.1:81/api/locales_comida/",
            auth=(usuario, clave))
    cant_locales_comida = json.loads(rc.content)['count']
    rr = requests.get("http://127.0.0.1:81/api/locales_repuestos/",
            auth=(usuario, clave))
    cant_locales_repuestos = json.loads(rr.content)['count']
    return render_template("index.html", now=now, cant_locales_comida=cant_locales_comida,
        cant_locales_repuestos=cant_locales_repuestos, cant_personas=cant_personas, cant_barrios=cant_barrios)

@app.route("/personas")
def personas():
    r = requests.get("http://127.0.0.1:81/api/personas/",
            auth=(usuario, clave))
    personas = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("personas.html", personas=personas,
        numero=numero)

@app.route("/barrios")
def barrios():
    r = requests.get("http://127.0.0.1:81/api/barrios/",
            auth=(usuario, clave))
    barrios = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("barrios.html", barrios=barrios,
        numero=numero)

@app.route("/locales/comida")
def locales_comida():
    r = requests.get("http://127.0.0.1:81/api/locales_comida/",
            auth=(usuario, clave))
    locales_comida = json.loads(r.content)['results']
    cant_locales_comida = json.loads(r.content)['count']
    return render_template("localescomida.html", locales_comida=locales_comida,
        cant_locales_comida=cant_locales_comida)


@app.route("/locales/repuestos")
def locales_repuestos():
    r = requests.get("http://127.0.0.1:81/api/locales_repuestos/",
            auth=(usuario, clave))
    locales_repuestos = json.loads(r.content)['results']
    cant_locales_repuestos = json.loads(r.content)['count']
    return render_template("localesrepuestos.html", locales_repuestos=locales_repuestos,
        cant_locales_repuestos=cant_locales_repuestos)
