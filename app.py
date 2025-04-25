
from flask import Flask, render_template
import os
import logging

# Corrigir conflitos com arquivo 'logs'
if os.path.isfile("logs"):
    os.remove("logs")
os.makedirs("logs", exist_ok=True)

# Logging

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

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/pagamento")
def pagamento():
    return render_template("pagamento.html")


from flask import Flask, render_template

app = Flask(__name__)




if __name__ == "__main__":
    app.run(debug=True)
