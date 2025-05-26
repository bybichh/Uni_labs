# Список продажів
sales = []

# Введення користувача
while True:
    name = input("Enter product name or write stop: ").strip().lower()
    if name == "stop":
        break
    try:
        amount = int(input("Enter quantity: "))
        cost = float(input("Enter price per one: "))
        sales.append({"name": name, "amount": amount, "cost": cost})
    except ValueError:
        print("Invalid number")

# Підрахунок доходу по кожному продукту
def count_income(data):
    income = {}
    for item in data:
        product = item["name"]
        total = item["amount"] * item["cost"]
        income[product] = income.get(product, 0) + total
    return income

# Загальний дохід
all_income = count_income(sales)

# Продукти з доходом більше 1000
top_products = [p for p, val in all_income.items() if val > 1000]

# Результат
print("Total income per product:", all_income)
print("Products with income over 1000:", top_products)
