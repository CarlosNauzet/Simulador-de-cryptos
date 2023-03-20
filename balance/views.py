from . import app


@app.route('/')
def inicio():
    return 'Nauzet va a crear un API para el proyecto de fin de bootcamp'