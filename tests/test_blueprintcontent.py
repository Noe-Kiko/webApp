"""This is a test script to test flask application"""
import pytest
from application import init_app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    app = init_app()
    with app.test_client() as app_client:
        yield app_client

def test_main_page_content(client):
    """flask unit testing for content in default page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Our Flask Web Application" in response.data

def test_about_page_content(client):
    """flask unit testing for content in about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About This Project" in response.data 