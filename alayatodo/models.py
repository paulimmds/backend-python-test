from alayatodo import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import validates

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    todos = db.relationship('Todo', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Todo(db.Model):
    __tablename__ = 'Todo'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    description = db.Column(db.String(255), nullable=False)

    @validates('description')
    def description_validation(self, key, description):
        assert not description.isspace(), 'Description can not be only white space.'
        assert description != '', 'Description can not be empty.'
        return description
        
@login.user_loader
def load_user(id):
    return User.query.get(int(id))