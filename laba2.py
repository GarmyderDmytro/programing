# база користувачів
users = {
    "ivan": {
        "password": "1234",
        "grades": [10, 12, 7, 9, 3, 11]
    },
    "olena": {
        "password": "qwerty",
        "grades": [5, 6, 2, 8, 4, 12, 1]
    },
    "petro": {
        "password": "pass123",
        "grades": [3, 7, 9, 10, 2, 6]
    },
    "maria": {
        "password": "abcd",
        "grades": [12, 11, 5, 4, 1, 8, 9]
    }
}

print("Вхід до системи")
login = input("Логін: ")
password = input("Пароль: ")

user = users.get(login)

if user is None or user["password"] != password:
    print("Невірний логін або пароль.")
else:
    grades = user["grades"]

    print(f"\nВітаємо, {login}!")
    print("Ваші оцінки:", grades)

    satisfactory = [g for g in grades if 5 <= g <= 12]
    unsatisfactory = [g for g in grades if 1 <= g <= 4]

    print(f"\nЗадовільних оцінок (5-12): {len(satisfactory)}")
    print(f"Незадовільних оцінок (1-4): {len(unsatisfactory)}")
