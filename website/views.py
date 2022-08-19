from flask import Blueprint, render_template, flash, request
from . import db
from .models import Reserva

views = Blueprint('views', __name__)  #8 define blueprint


@views.route('/', methods=['GET', 'POST'])  #7 roda sempre que formos pra essa route
def agenda():
    if request.method == 'POST':
        numero = request.form.get('numero')
        
        
        numero = Reserva.query.filter_by(numero=numero).first()

        if numero:
            flash('Sala já reservada.', category='error')

        
        else:
            db.drop_all()
            db.create_all()
            nova_reserva = Reserva(numero=numero)
            db.session.add(nova_reserva)
            db.session.commit()
            flash('Reserva criada!', category='success')
    return render_template('agenda.html')
