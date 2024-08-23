import requests
import pytest
from main1 import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    # Мок успешного запроса
    mock_get = mocker.patch('main1.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/example.jpg'}
    ]

    image_url = get_random_cat_image()
    assert image_url == 'https://cdn2.thecatapi.com/images/example.jpg'

def test_get_random_cat_image_404(mocker):
    # Мок запроса с кодом ошибки 404
    mock_get = mocker.patch('main1.requests.get')
    mock_get.return_value.status_code = 404

    image_url = get_random_cat_image()
    assert image_url is None

def test_get_random_cat_image_no_url_in_response(mocker):
    # Мок успешного запроса, но без 'url' в ответе
    mock_get = mocker.patch('main1.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{}]

    image_url = get_random_cat_image()
    assert image_url is None

def test_get_random_cat_image_network_error(mocker):
    # Мок ошибки сети или подключения
    mock_get = mocker.patch('main1.requests.get', side_effect=requests.RequestException("Network error"))

    image_url = get_random_cat_image()
    assert image_url is None
