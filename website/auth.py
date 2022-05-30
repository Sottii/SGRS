#5 coisas relacionadas à autenticação 

import email
from flask import Blueprint, flash, render_template, redirect, url_for, request

from website import views
from .models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from . import db



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    return redirect(url_for('views.agenda'))

@auth.route('/cadastrar-usuario', methods=['POST', 'GET'])
def cadastrar_usuario():
        return render_template('cadastrar-usuario.html')

@auth.route('/cadastrar-sala', methods=['POST', 'GET'])
def cadastrar_sala():
    return render_template('cadastrar-sala.html')

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        if senha1 != senha2:
            flash('Senhas não conferem.', category='error')
        elif len(senha1) < 8:
            flash('Senha menor que 8 caracteres.', category='error')
        elif len(email) < 6:
            flash('Email muito curto.', category='error')
        else:
            new_user = Usuario(email=email, nome=nome, senha=generate_password_hash(senha1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Bem vindo! \nAgora faça login.', category='success')
            return redirect(url_for('views.agenda'))

    return render_template('sign-up.html')
