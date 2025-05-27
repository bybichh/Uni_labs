import requests
import json
import matplotlib.pyplot as plt

# Запит до НБУ
nbu_response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250520&end=20250527&valcode=usd&sort=exchangedate&order=desc&json')
data = json.loads(nbu_response.content)

# Обробка
exchange_dates = [item['exchangedate'] for item in reversed(data)]
exchange_rates = [item['rate'] for item in reversed(data)]

# Графік
plt.plot(exchange_dates, exchange_rates, marker='o')
plt.xlabel("Дата")
plt.ylabel("Курс USD")
plt.title("Курс USD за 20–27 травня 2025")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
