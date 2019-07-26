from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('home.html')

@core.route('/info')
def info():
    return render_template('info.html')

@core.route('/contact')
def contact():
    return render_template('contact.html')
