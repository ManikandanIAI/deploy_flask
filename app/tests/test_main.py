import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Guess the Number!' in rv.data

def test_index_post_valid_guess(client):
    with client.session_transaction() as sess:
        sess['number'] = 50
        sess['guesses'] = 0
    rv = client.post('/', data={'guess': '40'})
    assert rv.status_code == 200
    assert b'Too low!' in rv.data
