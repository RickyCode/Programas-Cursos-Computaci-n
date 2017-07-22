from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return '<h1> HOLA MUNDO</h1>'

@app.route('programacion_basico')
def programacion_basico():
    return '<h1>Curso de Programación Básico</h1>'


