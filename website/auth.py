#5 coisas relacionadas à autenticação 

import email
from flask import Blueprint, flash, render_template, redirect, url_for, request

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
            flash('Bem vindo!', category='success')

    return render_template('sign-up.html')
