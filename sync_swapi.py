from main import app
from datetime import datetime
import requests

while True:
    answer = input("Добавление стать(post)/Удаление статьи(del)/Изменить Статью(put)/Просмотор статьи(get)/выйти(0)")
    if answer == "post":

        title = input("Введите заголовок")
        description = input("Введите тему статьи")
        creation_date = datetime.now().date()
        owner = input("Введите логин")

        response = requests.post(
            'http://127.0.0.1:5000/ad',
                json={
                  "title": str(title),
                  "description": str(description),
                  "creation_date": str(creation_date),
                  "owner": str(owner)
                }
            )
        updated_ad = response.json()
        print("Добавлена статья:", updated_ad)

    elif answer == "get":
        id = input("Введите id")
        response = requests.get('http://127.0.0.1:5000/ad/'+id)
        updated_ad = response.json()
        print(f"Статья номер{id}:", updated_ad)

    elif answer == "del":
        id = input("Введите id")
        response = requests.get('http://127.0.0.1:5000/ad/' + id)
        print(response.status_code)

    elif answer == "put":
        id = input("Введите id")
        title = input("Введите заголовок")
        description = input("Введите тему статьи")
        creation_date = datetime.now().date()
        owner = input("Введите логин")

        response = requests.put(
            'http://127.0.0.1:5000/ad/'+id,
                json={
                  "title": str(title),
                  "description": str(description),
                  "creation_date": str(creation_date),
                  "owner": str(owner)
                }
            )
        updated_ad = response.json()
        print("Обновленная статья:", updated_ad)

    elif answer == str(0):
        break

    else:
        print("я не знаю такой команды")

