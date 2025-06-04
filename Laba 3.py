import sqlite3
import hashlib

# Підключення до БД (створення або відкриття існуючої)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Створення таблиці користувачів, якщо вона ще не існує
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    login TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    full_name TEXT NOT NULL)''')
conn.commit()

# Функція для хешування пароля з використанням SHA-256

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Функція для додавання нового користувача

def add_user():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    full_name = input("Введіть повне ім'я: ")
    try:
        cursor.execute('INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)',
                       (login, hash_password(password), full_name))
        conn.commit()
        print("Користувача додано успішно.")
    except sqlite3.IntegrityError:
        print("Користувач з таким логіном вже існує.")

# Функція для оновлення пароля користувача

def update_password():
    login = input("Введіть логін користувача: ")
    new_password = input("Введіть новий пароль: ")
    cursor.execute('UPDATE users SET password = ? WHERE login = ?',
                   (hash_password(new_password), login))
    if cursor.rowcount == 0:
        print("Користувача не знайдено.")
    else:
        conn.commit()
        print("Пароль оновлено успішно.")

# Функція для перевірки автентифікації користувача

def authenticate_user():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    cursor.execute('SELECT password FROM users WHERE login = ?', (login,))
    result = cursor.fetchone()
    if result and result[0] == hash_password(password):
        print("Автентифікація пройшла успішно.")
    else:
        print("Невірний логін або пароль.")

# Головне меню для взаємодії з програмою
if __name__ == '__main__':
    while True:
        print("\nМеню:")
        print("1. Додати нового користувача")
        print("2. Оновити пароль користувача")
        print("3. Перевірити автентифікацію")
        print("4. Вийти")
        choice = input("Виберіть опцію (1-4): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            update_password()
        elif choice == '3':
            authenticate_user()
        elif choice == '4':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Закриття з'єднання з БД після завершення програми
conn.close()
