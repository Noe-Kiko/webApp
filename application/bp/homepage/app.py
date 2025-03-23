"""
Homepage Blueprint
"""
from flask import Blueprint, render_template
from application.database import User
import traceback

bp = Blueprint('homepage', __name__)

@bp.route('/')
def index():
    """Homepage route"""
    return render_template('homepage.html')

@bp.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@bp.route('/users')
def users():
    """Users page route"""
    try:
        users = User.query.all()
        print(f"Found {len(users)} users")
        return render_template('users.html', users=users)
    except Exception as e:
        print(f"Error in users route: {str(e)}")
        print(traceback.format_exc())
        raise

