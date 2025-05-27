def filter_ips(input_file_path, output_file_path, allowed_ips):
    counts = {}  # Словник для підрахунку входжень дозволених IP

    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.split()
                if not parts:
                    continue  # Пропускаємо порожній рядок
                ip = parts[0]
                if ip in allowed_ips:
                    counts[ip] = counts.get(ip, 0) + 1  # Збільшуємо лічильник

        with open(output_file_path, 'w', encoding='utf-8') as out:
            for ip, count in counts.items():
                out.write(f"{ip} - {count}\n")  # Записуємо результати у файл

    except FileNotFoundError:
        print(f"Помилка, файл не знайдено: {input_file_path}")
    except IOError as err:
        print(f"Помилка, проблема з читанням файлу: {err}")

# Список дозволених IP-адрес
allowed_ips = ['93.114.45.13', '110.136.166.128', '208.115.111.72']

# Виклик функції з заданими файлами
filter_ips('apache_logs.txt', 'filtered_ips.txt', allowed_ips)
print("Готово: filtered_ips.txt")
