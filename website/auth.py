#5 coisas relacionadas à autenticação 
from os import access
from re import I
from flask import Blueprint, flash, render_template, redirect, url_for, request
from .models import Reserva, Usuario, Cadastrar
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user




auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        nome = request.form.get('nome')

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario:
            if check_password_hash(usuario.senha, senha):
                flash('Bem vindo!', category='success')
                login_user(usuario, remember=True)

                return redirect(url_for('views.agenda'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('Email não existente.', category='error')
    return render_template('login.html', usuario=current_user)

@auth.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('views.agenda'))

@auth.route('/cadastrar-sala', methods=['POST', 'GET'])
@login_required

def cadastrar_sala():
    
        if request.method == 'POST':
            numero = request.form.get('numero')
            projetor = request.form.get('numero')
            bloco = request.form.get('numero')
            andar = request.form.get('numero')
            tipo_quadro = request.form.get('numero')
            ac = request.form.get('numero')
            
            numero = Cadastrar.query.filter_by(numero=numero).first()

            if numero:
                flash('Sala já cadastrada.', category='error')
            
            elif projetor & bloco & andar & tipo_quadro & ac == None:
                flash('Sala já cadastrada.', category='error')
                
            
            else:
                db.drop_all()
                db.create_all()
                novo_cadastro = Cadastrar(numero=numero)
                db.session.add(novo_cadastro)
                db.session.commit()
                flash('Sala Cadastrada!', category='success')
                
        return render_template('cadastrar-sala.html')
    

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        tipoa = request.form.get('tipoa')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        if:
            
            
        if tipoa.checked:
            global i 
            i = 1
            
        if usuario:
            flash('Este email já existe.', category='error')

        elif '@ifpr.edu.br'not in email:
            flash('Email não institucional.', category='error')
            pass

        elif senha1 != senha2:
            flash('Senhas não conferem.', category='error')

        elif len(senha1) < 8:
            flash('Senha menor que 8 caracteres.', category='error')

        else:
            db.drop_all()
            db.create_all()
            new_user = Usuario(email=email, nome=nome, senha=generate_password_hash(senha1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(usuario, remember=True)
            flash('Conta criada! Agora faça login.', category='success')

            return redirect(url_for('auth.login', usuario=current_user))

    return render_template('sign-up.html', usuario=current_user)
