import hashlib
from datetime import datetime

# Хешування пароля
def encrypt_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

# Базовий клас користувача
class User:
    def __init__(self, username, password, active=True):
        self.username = username
        self.password_hash = encrypt_password(password)
        self.is_active = active

    def verify_password(self, password_input):
        return self.password_hash == encrypt_password(password_input)

# Адміністратор
class Administrator(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.permissions = ["ban_users", "edit_config", "view_all"]

# Звичайний користувач
class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login_time = None

    def update_last_login(self):
        self.last_login_time = datetime.now()

# Гість
class GuestUser(User):
    def __init__(self, username):
        super().__init__(username, "guest", active=False)

# Система доступу
class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user_obj):
        if user_obj.username not in self.users:
            self.users[user_obj.username] = user_obj
            print(f"[INFO] Користувач '{user_obj.username}' доданий.")
        else:
            print("[WARN] Такий користувач вже є.")

    def authenticate_user(self, uname, pwd):
        usr = self.users.get(uname)
        if usr and usr.verify_password(pwd):
            print(f"[SUCCESS] Вхід успішний як '{uname}'")
            if isinstance(usr, RegularUser):
                usr.update_last_login()
            return usr
        else:
            print("[FAIL] Дані не підходять.")
            return None

# Меню адміну
def show_admin_menu(admin):
    while True:
        print("\n=== Меню адміністратора ===")
        print("1. Показати дозволи")
        print("2. Вийти")
        choice = input(">> ")
        if choice == "1":
            print("\n[PERMISSIONS]:")
            for p in admin.permissions:
                print(f"- {p}")
        elif choice == "2":
            break
        else:
            print("[!] Хибний вибір")

# Меню користувача
def show_user_menu(user):
    while True:
        print("\n=== Меню користувача ===")
        print("1. Останній вхід")
        print("2. Вийти")
        choice = input(">> ")
        if choice == "1":
            if user.last_login_time:
                print(f"Останній логін: {user.last_login_time}")
            else:
                print("Це перший вхід.")
        elif choice == "2":
            break
        else:
            print("[!] Хибний вибір")

# Інфо для гостя
def show_guest_info(guest):
    print("\n[Гостьовий доступ]")
    print(f"Користувач: {guest.username}")
    print("Статус: тимчасовий, лише читання")
    print("Активний:", guest.is_active)

# Головна програма
if __name__ == "__main__":
    access = AccessControl()

    # Додаємо тестових користувачів
    access.add_user(Administrator("admin", "adminpass"))
    access.add_user(RegularUser("lexa", "mypass"))
    access.add_user(GuestUser("visitor"))

    print("\n--- Вхід у систему ---")
    login_input = input("Логін: ")

    # Гість — пароль не потрібен
    if login_input in access.users and isinstance(access.users[login_input], GuestUser):
        logged_user = access.authenticate_user(login_input, "guest")
    else:
        pass_input = input("Пароль: ")
        logged_user = access.authenticate_user(login_input, pass_input)

    # Меню залежно від типу користувача
    if isinstance(logged_user, Administrator):
        show_admin_menu(logged_user)
    elif isinstance(logged_user, RegularUser):
        show_user_menu(logged_user)
    elif isinstance(logged_user, GuestUser):
        show_guest_info(logged_user)
