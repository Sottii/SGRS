from flask import Flask


def criar_app():
    app = Flask(__name__)  #1 Inicializa o Flask
    app.config['SECRET_KEY'] = 'steven universo' #2 encrypt cookies e dados da sesssão

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app 
    