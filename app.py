
import os
import logging

# Garantir que o diretório de logs exista
os.makedirs("logs", exist_ok=True)

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
git config --global user.name "Seu Nome"