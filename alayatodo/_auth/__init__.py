from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)

from alayatodo._auth import routes