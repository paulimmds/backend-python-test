from alayatodo._home import home_bp
from flask import render_template

@home_bp.route('/')
def home():
    with home_bp.open_resource('../../README.md', mode='r') as f:
        readme = f.read()
        return render_template('index.html', readme=readme)
