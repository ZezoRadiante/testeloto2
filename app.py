
import os
import logging

# Garantir que o diretório de logs exista
if os.path.isfile("logs"):
    os.remove("logs")  # Deleta o arquivo com nome "logs"

os.makedirs("logs", exist_ok=True)  # Agora sim, cria a pasta

# Configurar logging para arquivo relativo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/app.log',
    filemode='a'
)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Aplicação Flask funcionando corretamente!"

if __name__ == "__main__":
    app.run(debug=True)
