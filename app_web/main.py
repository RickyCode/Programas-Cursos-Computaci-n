from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def principal():
    with open('pagina_principal.html') as archivo:
        pagina = archivo.read()
    return pagina

@app.route('/programacion_basico')
def programacion_basico():
    return '<h1>Curso de Programación Básico</h1>'


@app.route('/programacion_basico/git_webhook', methods=['POST'])
def git_webhook_post():
    recibido = request.json
    return 'Se recibió la información'

@app.route('/programacion_basico/git_webhook', methods=['GET'])
def git_webhook_get():
    return 'Esta página recibe los avisos de todos los cambios en los repositorios de los estudiantes.'