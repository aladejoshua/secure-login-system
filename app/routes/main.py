#Other routes (e.g., dashboard after login)
from flask import Blueprint, request, render_template
from .. import db
from ..models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'User registered!'
    return render_template('register.html')