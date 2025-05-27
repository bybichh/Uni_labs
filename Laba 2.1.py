import re

def analyze_log_file(log_file_path):
    # Створення словника для зберігання кількості кожного коду
    stats = dict()

    try:
        with open(log_file_path, encoding='utf-8') as f:
            for line in f:
                result = re.search(r'"\s*(\d{3})\s', line)
                if result:
                    code = result.group(1)
                    stats[code] = stats.get(code, 0) + 1

    except FileNotFoundError:
        # Повідомлення, якщо файл не знайдено
        print(f"Помилка, файл не знайдено: {log_file_path}")
    except IOError as err:
        # Повідомлення, якщо сталася інша помилка читання
        print(f"Помилка, проблема з читанням файлу {log_file_path}: {err}")

    return stats

# Приклад використання
log_file = 'apache_logs.txt'
response_stats = analyze_log_file(log_file)

# Вивід результатів у зростаючому порядку кодів
for status_code in sorted(response_stats):
    print(f"HTTP {status_code}: {response_stats[status_code]} разів")

