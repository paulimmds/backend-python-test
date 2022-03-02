from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)

from alayatodo._home import routes