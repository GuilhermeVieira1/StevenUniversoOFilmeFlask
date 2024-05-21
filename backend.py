from flask import Flask
from werkzeug.serving import run_simple
from rotas.main import main
from rotas.elenco import elenco

app = Flask(__name__, template_folder='paginas', static_folder='static')

app.register_blueprint(main)
app.register_blueprint(elenco)

if __name__ == "__main__":
   run_simple('0.0.0.0', 3000, app, use_reloader = True)