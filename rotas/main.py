from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def Main():
    return render_template('index.html') 