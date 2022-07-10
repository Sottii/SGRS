from flask import Blueprint, render_template#6 blueprint = tem muitas urls definidas

views = Blueprint('views', __name__)  #8 define blueprint


@views.route('/')  #7 roda sempre que formos pra essa route
def agenda():
    return render_template('agenda.html')
