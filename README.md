# Gerador de Jogos da Lotofácil

Sistema completo para geração de jogos da Lotofácil com estratégias avançadas e IA LSTM.

## Requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Navegador web moderno

## Instalação

1. Extraia o conteúdo do pacote em um diretório de sua escolha
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

1. Edite o arquivo `scripts/pagamento/mercadopago_integration.py` e verifique se a chave PIX está correta:

```python
self.pix_key = "42f51e7f-7586-4f26-a5b2-837ef34a0bfb"  # Chave PIX
```

2. Crie os diretórios necessários:

```bash
mkdir -p logs data/pagamentos data/usuarios data/emails data/modelos data/estrategias
```

## Inicialização

Para iniciar todos os serviços:

```bash
python scripts/main.py start
```

Para iniciar apenas serviços específicos:

```bash
python scripts/main.py start --services payment lstm ciclo auth
```

## Acesso

Após iniciar os serviços, acesse o sistema em:

```
http://localhost:5004
```

## Gerenciamento

- Verificar status dos serviços: `python scripts/main.py status`
- Parar serviços: `python scripts/main.py stop`
- Reiniciar serviços: `python scripts/main.py restart`
- Executar testes: `python scripts/main.py test`

## Estrutura do Sistema

- `app.py`: Aplicação principal
- `scripts/`: Scripts do sistema
  - `auth/`: Sistema de autenticação
  - `pagamento/`: Sistema de pagamento
  - `ia/`: IA LSTM para análise de dados
  - `estrategias/`: Estratégias de jogo, incluindo ciclo de dezenas fora
  - `test/`: Scripts de teste
- `templates/`: Templates HTML
- `static/`: Arquivos estáticos (CSS, JS, imagens)
- `data/`: Dados do sistema

## Planos de Assinatura

- Básico: R$ 39,90/mês
- Premium: R$ 69,90/mês (inclui estratégia exclusiva de ciclo de dezenas fora)

## Suporte

Para suporte, entre em contato pelo e-mail: suporte@geradorlotofacil.com.br
