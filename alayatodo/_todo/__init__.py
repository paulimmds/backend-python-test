from flask import Blueprint

todo_bp = Blueprint('todo_bp', __name__)

from alayatodo._todo import routes