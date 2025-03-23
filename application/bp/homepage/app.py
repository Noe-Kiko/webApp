"""
Homepage Blueprint
"""
from flask import Blueprint, render_template
from application.database import User

bp = Blueprint('homepage', __name__)

@bp.route('/')
def index():
    """Homepage route"""
    return render_template('homepage/homepage.html')

@bp.route('/about')
def about():
    """About page route"""
    return render_template('homepage/about.html')

@bp.route('/users')
def users():
    """Users page route"""
    users = User.all()
    return render_template('homepage/users.html', users=users)

