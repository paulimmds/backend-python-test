from alayatodo._auth import auth_bp
from flask import render_template, request, session, redirect
from alayatodo.models import User
from alayatodo import db

@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@auth_bp.route('/register/<username>/<password>', methods=['GET','POST'])
def register(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return redirect('/')

@auth_bp.route('/login', methods=['POST'])
def login_POST():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    if user:
        user = {
            'id': user.id,
            'username': user.username,
            'password': user.password
        }
        session['user'] = user
        session['logged_in'] = True
        return redirect('/todo')

    return redirect('/login')

@auth_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect('/')