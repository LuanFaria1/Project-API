from . import db

# Entidade Professor
class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.String(255))

    # Relacionamento One-to-Many (um professor pode ter muitas turmas)
    turmas = db.relationship('Turma', backref='professor', lazy=True)

# Entidade Turma
class Turma(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    # Chave estrangeira para Professor (One-to-Many)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)

    # Relacionamento One-to-Many com Aluno
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

# Entidade Aluno
class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)

    # Chave estrangeira para Turma (One-to-Many)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
