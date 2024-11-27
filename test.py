import pytest
from main import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value =  [{
        'id': 'yKXeUMNZ8',
        'url': 'https://cdn2.thecatapi.com/images/yKXeUMNZ8.jpg',
        'width': 1080,
        'height': 1350
    }]

    url = "https://api.thecatapi.com/v1/images/search"
    cat_image_data = get_random_cat_image(url)

    assert cat_image_data == [{
        'id': 'yKXeUMNZ8',
        'url': 'https://cdn2.thecatapi.com/images/yKXeUMNZ8.jpg',
        'width': 1080,
        'height': 1350
    }]




def test_get_random_cat_image_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = None

    url = "https://api.thecatapi.com/url_error"
    cat_image_data = get_random_cat_image(url)

    assert cat_image_data == None
