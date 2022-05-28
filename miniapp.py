#importarmas la libreria flask
from flask import Flask, render_template

#incializamos la variable
app = Flask(__name__, template_folder= 'templates')


#ruta - Página principal
@app.route('/')
def pag_principal():
    return render_template('main.html')


#main del programa
if __name__ == '__main__':
    #debug = True, para reiniciar automáticamente el servidor.
    app.run(debug=True)