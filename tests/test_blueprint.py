"""This is a test script to test flask application"""
from application import init_app

def test_bp_usage():
    """Test if there is blueprint registered"""
    app = init_app()
    assert app.blueprints.keys(), "No Blueprint Registered!" 