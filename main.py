import requests

def get_random_cat_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Преобразование ответа в JSON
        return data
    else:
        return None

# Пример использования функции
if __name__ == "__main__":
    url = "https://api.thecatapi.com/v1/images/search"
    cat_image = get_random_cat_image(url)
    cat_image_url = cat_image[0]['url']  # Получение URL изображения
    if cat_image:
        print("Случайное изображение кошки:", cat_image)