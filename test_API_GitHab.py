import pytest
import requests

from main_API_GitHab import get_githab_user

def test_get_githab_user(mocker):
    mock_get = mocker.patch('main_API_GitHab.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name' : 'Anna'
    }

    user_data = get_githab_user('cat')

    assert user_data == {
        'login': 'nizavr',
        'id': 345178,
        'name' : 'Anna'
    }

def test_get_githab_user_with_error(mocker):
    mock_get = mocker.patch('main_API_GitHab.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = None

    user_data = get_githab_user('cat')

    assert user_data == None