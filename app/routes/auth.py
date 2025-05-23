from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)
main_bp = Blueprint('main', __name__)

@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/register')
def register():
    return render_template('register.html')

@auth_bp.route('/2fa_setup')
def tfa ():
    return render_template('2fa_setup.html')

@auth_bp.route('/2fa_verfiy')
def tfa_v ():
    return render_template('2fa_verify.html')

@auth_bp.route('/dashboard')
def dashboard ():
    return render_template('dashboard.html')
