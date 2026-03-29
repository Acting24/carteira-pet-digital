from flask import Blueprint, render_template, request, jsonify
from datetime import datetime

# Criar blueprint para rotas principais
bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    """Página inicial do sistema"""
    return render_template('index.html', title='Início')

@bp.route('/sobre')
def sobre():
    """Página sobre o projeto"""
    info_projeto = {
        'nome': 'Carteira Digital Pet',
        'descricao': 'Sistema web para gerenciamento de vacinação de pets',
        'versao': '1.0.0',
        'disciplina': 'PJI110 - Projeto Integrador em Computação I',
        'instituicao': 'UNIVESP',
        'ano': 2026
    }
    return render_template('sobre.html', title='Sobre', projeto=info_projeto)

@bp.route('/api/status')
def api_status():
    """Endpoint de API para verificar status do sistema"""
    return jsonify({
        'status': 'online',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat(),
        'message': 'Carteira Digital Pet - Sistema operacional'
    })

@bp.route('/hello')
def hello_world():
    """Rota Hello World básica para testes"""
    return '''
    <html>
        <head>
            <title>Carteira Digital Pet - Hello World</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    margin: 50px; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-align: center;
                }
                .container { 
                    background: rgba(255,255,255,0.1); 
                    padding: 30px; 
                    border-radius: 10px; 
                    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                }
                h1 { color: #FFD700; margin-bottom: 20px; }
                .emoji { font-size: 3em; margin: 20px 0; }
                .info { 
                    background: rgba(255,255,255,0.2); 
                    padding: 20px; 
                    border-radius: 5px; 
                    margin: 20px 0;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="emoji">🐕🐱💉</div>
                <h1>Carteira Digital Pet</h1>
                <h2>Hello World - Flask está funcionando!</h2>
                <div class="info">
                    <p><strong>Projeto:</strong> Sistema web para gerenciamento de vacinação de pets</p>
                    <p><strong>Disciplina:</strong> PJI110 - Projeto Integrador em Computação I</p>
                    <p><strong>Instituição:</strong> UNIVESP</p>
                    <p><strong>Framework:</strong> Flask + Python</p>
                    <p><strong>Status:</strong> ✅ Desenvolvimento iniciado!</p>
                </div>
                <p><em>Se você está vendo esta página, o Flask foi configurado corretamente!</em></p>
            </div>
        </body>
    </html>
    '''

@bp.route('/test')
def test_route():
    """Rota de teste para verificar se tudo está funcionando"""
    import sys
    import platform
    
    info_sistema = {
        'python_version': sys.version,
        'platform': platform.system(),
        'flask_working': True,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return jsonify(info_sistema)