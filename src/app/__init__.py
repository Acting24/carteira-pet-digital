from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config

# Extensões do Flask
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_name='default'):
    """Factory para criar e configurar a aplicação Flask"""
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    
    # Configurar LoginManager
    login.login_view = 'auth.login'
    login.login_message = 'Por favor, faça login para acessar esta página.'
    login.login_message_category = 'info'
    
    # Registrar blueprints
    from .routes.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Importar modelos para que sejam conhecidos pelo SQLAlchemy
    from .models import user, pet, vacina
    
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': user.User, 'Pet': pet.Pet, 'Vacina': vacina.Vacina}
    
    return app