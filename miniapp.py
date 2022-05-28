#importar la libreria flask
from flask import Flask, render_template, abort
#incializacion de la variable
app = Flask(__name__, template_folder= 'templates')


#ruta - Página principal
@app.route('/')
def pag_principal():
    return render_template('index.html')


#main del programa
if __name__ == '__main__':
    #debug = True, para reiniciar automáticamente el servidor
    app.run(debug=True)