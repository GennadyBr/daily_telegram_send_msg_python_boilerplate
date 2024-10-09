""" Test """
import requests


def test_async() -> None:
    """Test"""
    response = requests.get('https://open-meteo.com/en/docs')
    assert response.status_code == 200
