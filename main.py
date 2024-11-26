import requests
import pytest
from main import get_weather

def get_weather(api_key, city):
    url = f'[<http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}>](<http://api.openweathermap.org/data/2.5/weather?q=%7Bcity%7D&appid=%7Bapi_key%7D>)'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def test_get_weather_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {''}
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

    api_key = 'test_api_key'
    city = 'London'
    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }


