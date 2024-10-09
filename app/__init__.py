from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialize o SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Carregue as configurações do banco de dados
    app.config.from_object('app.config.Config')
    
    # Inicialize o banco de dados com a aplicação Flask
    db.init_app(app)
    
    # Registrar as rotas
    from .routes import main
    app.register_blueprint(main)
    
    return app