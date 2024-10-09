from flask import Blueprint, jsonify, request
from .models import Professor, Turma, Aluno, db

main = Blueprint('main', __name__)

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
    novo_aluno = Aluno(
        nome=data['nome'], 
        idade=data['idade'], 
        data_nascimento=data['data_nascimento'], 
        nota_primeiro_semestre=data['nota_primeiro_semestre'], 
        nota_segundo_semestre=data['nota_segundo_semestre'], 
        media_final=data['media_final'], 
        turma_id=data['turma_id']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno criado com sucesso'}), 201
