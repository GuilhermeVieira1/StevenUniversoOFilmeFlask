from flask import Blueprint, render_template

elenco = Blueprint('elenco', __name__)

@elenco.route('/elenco')
def Elenco():
    return render_template('elenco.html') 