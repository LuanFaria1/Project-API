from flask import Blueprint, jsonify, request, render_template
from datetime import datetime
from .models import Professor, Turma, Aluno, db

main = Blueprint('main', __name__)

# Rota para renderizar a página inicial
@main.route('/')
def index():
    return render_template('index.html')

# Rota para renderizar o formulário de cadastro de professor
@main.route('/cadastro_professor')
def cadastro_professor():
    return render_template('cadastro_professor.html')

# Rota para renderizar o formulário de cadastro de turma
@main.route('/cadastro_turma')
def cadastro_turma():
    return render_template('cadastro_turma.html')

# Rota para renderizar o formulário de cadastro de aluno
@main.route('/cadastro_aluno')
def cadastro_aluno():
    return render_template('cadastro_aluno.html')

# Rota para listar turmas
@main.route('/listar_turmas')
def listar_turmas():
    return render_template('listar_turmas.html')

# Rota para criar um novo professor
@main.route('/professor', methods=['POST'])
def create_professor():
    data = request.get_json()
    novo_professor = Professor(
        nome=data['nome'], 
        idade=data['idade'], 
        materia=data['materia'], 
        observacoes=data.get('observacoes', '')
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({'message': 'Professor criado com sucesso'}), 201

# Rota para criar uma nova turma
@main.route('/turma', methods=['POST'])
def create_turma():
    data = request.get_json()
    nova_turma = Turma(
        descricao=data['descricao'], 
        professor_id=data['professor_id'], 
        ativo=data.get('ativo', True)
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify({'message': 'Turma criada com sucesso'}), 201

# Rota para criar um novo aluno
@main.route('/aluno', methods=['POST'])
def create_aluno():
    data = request.get_json()
    
    try:
        # Converte a data de nascimento de string para objeto de data
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        
        novo_aluno = Aluno(
            nome=data['nome'], 
            idade=int(data['idade']), 
            data_nascimento=data_nascimento, 
            nota_primeiro_semestre=float(data['nota_primeiro_semestre']), 
            nota_segundo_semestre=float(data['nota_segundo_semestre']), 
            media_final=float(data['media_final']), 
            turma_id=int(data['turma_id'])
        )
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify({'message': 'Aluno criado com sucesso'}), 201
    
    except Exception as e:
        db.session.rollback()  # Reverte em caso de erro
        return jsonify({'error': str(e)}), 400

# Rota para carregar todos os professores
@main.route('/professores')
def listar_professores():
    professores = Professor.query.all()
    return jsonify([{'id': professor.id, 'nome': professor.nome} for professor in professores])

# Rota para carregar todas as turmas com seus professores e alunos
@main.route('/turmas')
def listar_turmas_data():
    turmas = Turma.query.all()
    result = []
    for turma in turmas:
        result.append({
            'id': turma.id,
            'descricao': turma.descricao,
            'professor': {'id': turma.professor.id, 'nome': turma.professor.nome},
            'alunos': [{'id': aluno.id, 'nome': aluno.nome} for aluno in turma.alunos]
        })
    return jsonify(result)
