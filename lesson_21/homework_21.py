"""
https://petstore.swagger.io/
Опис: Swagger Petstore - це відкрите API, яке надає можливість управляти даними про домашніх тварин. За допомогою цього API можна додавати нових тварин, знаходити тварин за ідентифікатором, виконувати замовлення на тварин та багато іншого.
Вам потрібно реалізувати програму, яка взаємодіє з Swagger Petstore API, використовуючи HTTP запити. Основні методи запитів, які вам знадобляться: GET, POST, PUT, DELETE.
**Ваші завдання:**
1. Отримати список доступних тварин (метод GET).
1. Зробіть запит до /pet/findByStatus з параметром status, щоб отримати список усіх тварин.
    1. Обробіть відповідь сервера та виведіть список тварин на екран.
1. Додати нову тварину (метод POST).
    Створіть новий об'єкт тварини з необхідною інформацією, наприклад, ім'я та статус.
    Зробіть запит до /pet з об'єктом тварини в тілі запиту, щоб додати нову тварину.
    Обробіть відповідь сервера та виведіть підтвердження про додавання тварини на екран.
1. Знайти тварину за ідентифікатором (метод GET).
    1. Введіть ідентифікатор тварини, яку потрібно знайти.
    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор шуканої тварини.
    1. Обробіть відповідь сервера та виведіть інформацію про знайдену тварину на екран.
1. Видалити тварину за ідентифікатором (метод DELETE).
    1. Введіть ідентифікатор тварини, яку потрібно видалити.
    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор тварини, яку потрібно видалити.
    1. Обробіть відпові
"""


import requests


BASE_URL = "https://petstore.swagger.io/v2"

def get_pets_by_status(status):
    url = f"{BASE_URL}/pet/findByStatus"
    response = requests.get(url, params={"status": status})
    if response.status_code == 200:
        pets = response.json()
        print(f"Pets with status '{status}':")
        for pet in pets:
            print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print(f"Failed to retrieve pets. Status code: {response.status_code}")

def add_new_pet(name, status):
    url = f"{BASE_URL}/pet"
    pet_data = {
        "id": 0,
        "name": name,
        "status": status
    }
    response = requests.post(url, json=pet_data)
    if response.status_code == 200 or response.status_code == 201:
        pet = response.json()
        print(f"Successfully added pet: ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print(f"Failed to add pet. Status code: {response.status_code}")

def get_pet_by_id(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    if response.status_code == 200:
        pet = response.json()
        print(f"Found pet: ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print(f"Failed to retrieve pet. Status code: {response.status_code}")

def delete_pet_by_id(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Successfully deleted pet with ID: {pet_id}")
    else:
        print(f"Failed to delete pet. Status code: {response.status_code}")

if __name__ == "__main__":
    # Отримати список доступних тварин
    status = input("Enter status to find pets (available, pending, sold): ")
    get_pets_by_status(status)

    # Додати нову тварину
    name = input("Enter the name of the new pet: ")
    status = input("Enter the status of the new pet (available, pending, sold): ")
    add_new_pet(name, status)

    # Знайти тварину за ідентифікатором
    pet_id = int(input("Enter the ID of the pet to find: "))
    get_pet_by_id(pet_id)

    # Видалити тварину за ідентифікатором
    pet_id = int(input("Enter the ID of the pet to delete: "))
    delete_pet_by_id(pet_id)
