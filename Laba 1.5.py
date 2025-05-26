import hashlib

# Хешування паролю
def hash_pass(pw):
    return hashlib.md5(pw.encode()).hexdigest()

# Користувачі
users = {
    "Oleksii": {
        "pass": hash_pass("Leksii_1487"),
        "name": "Oleksii Vadymovich Babych"
    },
    "Olya": {
        "pass": hash_pass("1488_Olyaya"),
        "name": "Olya Ivanovna Kaforenko"
    },
    "Stepan": {
        "pass": hash_pass("Stepa_stepa1482"),
        "name": "Stepan Petrovich Vaulov"
    }
}

# Перевірка
def check(login, pw):
    if login in users:
        if users[login]["pass"] == hash_pass(pw):
            print(f"Welcome, {users[login]['name']}!")
        else:
            print("Wrong password.")
    else:
        print("User not found.")

# Запуск
user = input("Login: ")
pw = input("Password: ")

check(user, pw)
