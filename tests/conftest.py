import pytest
import requests


@pytest.fixture()
def client():
    session = requests.Session()
    session.auth = ('admin', 'admin')
    session.headers.update({'Accept': 'application/json'})
    return session
