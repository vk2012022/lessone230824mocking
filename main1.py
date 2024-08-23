import requests

def get_random_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data and 'url' in data[0]:
                return data[0]['url']
            else:
                print("Ошибка: Нет данных или отсутствует поле 'url'.")
                return None
        else:
            print(f"Ошибка: API вернул код {response.status_code}.")
            return None
    except requests.RequestException as e:
        print(f"Ошибка сети или подключения: {e}")
        return None
