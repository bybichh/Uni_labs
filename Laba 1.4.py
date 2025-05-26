# Словник задач
todo = {}

# Статуси
status_list = {"1": "очікує", "2": "в процесі", "3": "виконано"}

# Додати
def add(task, stat = "очікує"):
    todo[task] = stat
    print(f"Додано '{task}' зі статусом '{stat}'.")

# Видалити
def delete(task):
    if task in todo:
        del todo[task]
        print(f"Видалено '{task}'.")
    else:
        print("Немає такої задачі.")

# Оновити статус
def change(task, stat):
    if task in todo:
        todo[task] = stat
        print(f"Статус '{task}' змінено на '{stat}'.")
    else:
        print("Немає такої задачі.")

# Показати задачі, що очікують
def waiting():
    pending = [t for t, s in todo.items() if s == "очікує"]
    print("Очікують:", pending)

# Меню
print("\n--- ЗАДАЧІ ---")
print("1. Додати")
print("2. Видалити")
print("3. Змінити статус")
print("4. Очікують")
print("5. Завершити")

while True:
    cmd = input("\nОпція: ")

    if cmd == "1":
        task = input("Назва: ")
        for k, v in status_list.items():
            print(f"{k}. {v}")
        stat = status_list.get(input("Статус: "), "очікує")
        add(task, stat)
    elif cmd == "2":
        delete(input("Назва: "))
    elif cmd == "3":
        task = input("Назва: ")
        for k, v in status_list.items():
            print(f"{k}. {v}")
        stat = status_list.get(input("Статус: "), "очікує")
        change(task, stat)
    elif cmd == "4":
        waiting()
    elif cmd == "5":
        print("Кінець. Усі задачі:", todo)
        waiting()
        break
    else:
        print("Хибна опція.")
