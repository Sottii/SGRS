from flask_login import current_user
from flask import Blueprint, render_template, flash, request
from . import db
from .models import Reserva

views = Blueprint('views', __name__)  #8 define blueprint


@views.route('/', methods=['GET', 'POST'])  #7 roda sempre que formos pra essa route
def agenda():
    if request.method == 'POST':
        numero = request.model.get('numero')
        new_reserva = Reserva(data=reserva, user_id=current_user.id)
        db.session.add(new_reserva)
        db.session.commit()
        flash('Reserva  realizada!', category='success')
    return render_template('agenda.html')
