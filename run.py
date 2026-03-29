#!/usr/bin/env python3
"""
Script principal para executar a aplicação Carteira Digital Pet

Como usar:
    python run.py

Para desenvolvimento com auto-reload:
    python run.py --debug
"""

import os
import sys
import argparse
from src.app import create_app

def main():
    """Função principal para iniciar a aplicação"""
    
    # Argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Carteira Digital Pet - Sistema Web')
    parser.add_argument('--debug', action='store_true', 
                       help='Executar em modo debug com auto-reload')
    parser.add_argument('--port', type=int, default=5000,
                       help='Porta para executar o servidor (padrão: 5000)')
    parser.add_argument('--host', type=str, default='127.0.0.1',
                       help='Host para executar o servidor (padrão: 127.0.0.1)')
    args = parser.parse_args()
    
    # Configurar ambiente
    if args.debug:
        os.environ['FLASK_ENV'] = 'development'
        config_name = 'development'
    else:
        config_name = os.environ.get('FLASK_CONFIG', 'default')
    
    # Criar aplicação
    app = create_app(config_name)
    
    # Mensagens informativas
    print("=" * 60)
    print("🐕 CARTEIRA DIGITAL PET - Sistema Web")
    print("=" * 60)
    print(f"📍 Servidor: http://{args.host}:{args.port}")
    print(f"🔧 Ambiente: {config_name}")
    print(f"🐛 Debug: {'Ativado' if args.debug else 'Desativado'}")
    print("=" * 60)
    print("📝 Para parar o servidor: Ctrl+C")
    print("=" * 60)
    
    # Executar aplicação
    try:
        app.run(
            host=args.host,
            port=args.port,
            debug=args.debug,
            use_reloader=args.debug
        )
    except KeyboardInterrupt:
        print("\n👋 Servidor finalizado. Até logo!")
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()