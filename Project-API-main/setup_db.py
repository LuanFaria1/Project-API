from app import create_app, db

# Inicialize a aplicação
app = create_app()

# Crie as tabelas no banco de dados
with app.app_context():
    db.create_all()
