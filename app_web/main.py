from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return '<h1>CURSOS DE COMPUTACION</h1>'

@app.route('/programacion_basico')
def programacion_basico():
    return '<h1>Curso de Programación Básico</h1>'


@app.route('/programacion_basico/git_webhook', methods=['POST','GET'])
def git_webhook():
    return 'Se recibió la información'