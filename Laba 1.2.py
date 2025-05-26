# Склад з продуктами
storage = {
    "maffine": 15,
    "pasta": 4,
    "tomato sauce": 2,
    "olive oil": 6,
    "pepsi": 3,
    "sausage": 1
}

# Оновлення кількості продукту
def update_storage(product, quantity):
    if product in storage:
        storage[product] += quantity
        if storage[product] < 0:
            storage[product] = 0
    else:
        storage[product] = max(0, quantity)

# Введення користувача
print("\n----- STORAGE -----")
while True:
    product = input("Enter product name or write stop: ").strip().lower()
    if product == "stop":
        break
    try:
        quantity = int(input("Enter quantity (+/-): "))
        update_storage(product, quantity)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Продукти з кількістю менше 5
low_stock = [name for name, qty in storage.items() if qty < 5]

# Вивід результату
print("Updated storage:", storage)
print("Products with less than 5 items:", low_stock)

