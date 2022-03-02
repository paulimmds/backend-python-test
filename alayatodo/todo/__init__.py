from flask import Blueprint

todo_bp = Blueprint('todo_bp', __name__)

from alayatodo.todo import routes