#5 coisas relacionadas à autenticação 
from crypt import methods
from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template('login.html', )

@auth.route('/logout')
def logout():
    return redirect(url_for('views.agenda'))

@auth.route('/cadastrar-usuario')
def cadastrar_usuario():
        return render_template('cadastrar-usuario.html')

@auth.route('/cadastrar-sala')
def cadastrar_sala():
    return render_template('cadastrar-sala.html')

@auth.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')
