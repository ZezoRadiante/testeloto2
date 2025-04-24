#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aplicação principal do Gerador de Jogos da Lotofácil
"""

import os
import sys
import logging
from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response
import subprocess
import json
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='/home/ubuntu/lotofacil/logs/app.log',
    filemode='a'
)
logger = logging.getLogger('app')

# Inicializar Flask
app = Flask(__name__, 
            template_folder='/home/ubuntu/lotofacil/templates',
            static_folder='/home/ubuntu/lotofacil/static')

# Importar middleware de autenticação
sys.path.append('/home/ubuntu/lotofacil/scripts/auth')
from auth_middleware import token_required, premium_required, html_token_required, html_premium_required

# Criar diretórios necessários
os.makedirs('/home/ubuntu/lotofacil/logs', exist_ok=True)

@app.route('/')
def index():
    """Rota para a página inicial"""
    return render_template('index.html')

@app.route('/login')
def login():
    """Rota para a página de login"""
    return render_template('login.html')

@app.route('/pagamento')
def pagamento():
    """Rota para a página de pagamento"""
    return render_template('pagamento.html')

@app.route('/dashboard')
@html_token_required
def dashboard():
    """Rota para o dashboard do usuário"""
    # Passar dados do usuário para o template
    user_data = request.user
    return render_template('dashboard.html', user=user_data)

@app.route('/ciclo-dezenas')
@html_token_required
@html_premium_required
def ciclo_dezenas():
    """Rota para a página de ciclo de dezenas fora (exclusiva para premium)"""
    # Passar dados do usuário para o template
    user_data = request.user
    return render_template('ciclo_dezenas.html', user=user_data)

@app.route('/api/proxy/payment/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@token_required
def proxy_payment(subpath):
    """Proxy para o serviço de pagamento"""
    try:
        import requests
        
        # URL do serviço
        service_url = f"http://localhost:5000/api/{subpath}"
        
        # Método da requisição
        method = request.method
        
        # Headers
        headers = {key: value for key, value in request.headers if key != 'Host'}
        if hasattr(request, 'user'):
            headers['X-User-Email'] = request.user.get('sub')
            headers['X-User-Plan'] = request.user.get('plan')
        
        # Dados
        data = request.get_data()
        
        # Fazer requisição
        if method == 'GET':
            response = requests.get(service_url, headers=headers, params=request.args)
        elif method == 'POST':
            response = requests.post(service_url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(service_url, headers=headers, data=data)
        elif method == 'DELETE':
            response = requests.delete(service_url, headers=headers)
        else:
            return jsonify({'error': 'Método não suportado'}), 405
        
        # Retornar resposta
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        logger.error(f"Erro no proxy para o serviço de pagamento: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/proxy/lstm/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@token_required
def proxy_lstm(subpath):
    """Proxy para o serviço de IA LSTM"""
    try:
        import requests
        
        # URL do serviço
        service_url = f"http://localhost:5001/api/{subpath}"
        
        # Método da requisição
        method = request.method
        
        # Headers
        headers = {key: value for key, value in request.headers if key != 'Host'}
        if hasattr(request, 'user'):
            headers['X-User-Email'] = request.user.get('sub')
            headers['X-User-Plan'] = request.user.get('plan')
        
        # Dados
        data = request.get_data()
        
        # Fazer requisição
        if method == 'GET':
            response = requests.get(service_url, headers=headers, params=request.args)
        elif method == 'POST':
            response = requests.post(service_url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(service_url, headers=headers, data=data)
        elif method == 'DELETE':
            response = requests.delete(service_url, headers=headers)
        else:
            return jsonify({'error': 'Método não suportado'}), 405
        
        # Retornar resposta
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        logger.error(f"Erro no proxy para o serviço de IA LSTM: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/proxy/ciclo/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@token_required
@premium_required
def proxy_ciclo(subpath):
    """Proxy para o serviço de ciclo de dezenas fora (exclusivo para premium)"""
    try:
        import requests
        
        # URL do serviço
        service_url = f"http://localhost:5002/api/{subpath}"
        
        # Método da requisição
        method = request.method
        
        # Headers
        headers = {key: value for key, value in request.headers if key != 'Host'}
        if hasattr(request, 'user'):
            headers['X-User-Email'] = request.user.get('sub')
            headers['X-User-Plan'] = request.user.get('plan')
        
        # Dados
        data = request.get_data()
        
        # Fazer requisição
        if method == 'GET':
            response = requests.get(service_url, headers=headers, params=request.args)
        elif method == 'POST':
            response = requests.post(service_url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(service_url, headers=headers, data=data)
        elif method == 'DELETE':
            response = requests.delete(service_url, headers=headers)
        else:
            return jsonify({'error': 'Método não suportado'}), 405
        
        # Retornar resposta
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        logger.error(f"Erro no proxy para o serviço de ciclo de dezenas fora: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/proxy/auth/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_auth(subpath):
    """Proxy para o serviço de autenticação"""
    try:
        import requests
        
        # URL do serviço
        service_url = f"http://localhost:5003/api/{subpath}"
        
        # Método da requisição
        method = request.method
        
        # Headers
        headers = {key: value for key, value in request.headers if key != 'Host'}
        if hasattr(request, 'user'):
            headers['X-User-Email'] = request.user.get('sub')
            headers['X-User-Plan'] = request.user.get('plan')
        
        # Dados
        data = request.get_data()
        
        # Fazer requisição
        if method == 'GET':
            response = requests.get(service_url, headers=headers, params=request.args)
        elif method == 'POST':
            response = requests.post(service_url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(service_url, headers=headers, data=data)
        elif method == 'DELETE':
            response = requests.delete(service_url, headers=headers)
        else:
            return jsonify({'error': 'Método não suportado'}), 405
        
        # Retornar resposta
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        logger.error(f"Erro no proxy para o serviço de autenticação: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/status')
def status():
    """Rota para verificar o status dos serviços"""
    try:
        # Executar script de verificação de status
        cmd = "cd /home/ubuntu/lotofacil && python3 scripts/main.py status"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Verificar resultado
        if process.returncode == 0:
            try:
                status = json.loads(stdout.decode('utf-8'))
                return jsonify(status)
            except Exception as e:
                logger.error(f"Erro ao parsear status: {str(e)}")
                return jsonify({'error': 'Erro ao parsear status'}), 500
        else:
            logger.error(f"Erro ao verificar status: {stderr.decode('utf-8')}")
            return jsonify({'error': stderr.decode('utf-8')}), 500
    except Exception as e:
        logger.error(f"Erro ao verificar status: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/restart/<service>', methods=['POST'])
@token_required
@premium_required
def restart_service(service):
    """Rota para reiniciar um serviço (exclusiva para premium)"""
    try:
        # Verificar se o serviço é válido
        valid_services = ['payment', 'lstm', 'ciclo', 'auth', 'main']
        if service not in valid_services and service != 'all':
            return jsonify({'error': 'Serviço inválido'}), 400
        
        # Executar script de reinicialização
        cmd = f"cd /home/ubuntu/lotofacil && python3 scripts/main.py restart {'' if service == 'all' else '--services ' + service}"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Verificar resultado
        if process.returncode == 0:
            try:
                result = json.loads(stdout.decode('utf-8'))
                return jsonify(result)
            except Exception as e:
                logger.error(f"Erro ao parsear resultado: {str(e)}")
                return jsonify({'error': 'Erro ao parsear resultado'}), 500
        else:
            logger.error(f"Erro ao reiniciar serviço: {stderr.decode('utf-8')}")
            return jsonify({'error': stderr.decode('utf-8')}), 500
    except Exception as e:
        logger.error(f"Erro ao reiniciar serviço: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Iniciar servidor Flask
    app.run(host='0.0.0.0', port=5004, debug=True)
