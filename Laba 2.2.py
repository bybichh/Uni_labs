import hashlib  # Для обчислення SHA-256 хешів

def generate_file_hashes(*file_paths):
    # Створення словника для збереження хешів
    file_hashes = dict()

    for filepath in file_paths:
        try:
            with open(filepath, 'rb') as file:
                data = file.read()
                sha256_hash = hashlib.sha256(data).hexdigest()
                file_hashes[filepath] = sha256_hash
        except FileNotFoundError:
            print(f"Помилка, файл не знайдено: {filepath}")
        except IOError as err:
            print(f"Помилка, проблема з читанням файлу {filepath}: {err}")

    return file_hashes

# Приклад використання
file_hashes = generate_file_hashes("apache_logs.txt", "data.txt")

# Вивід результатів
for filepath in sorted(file_hashes):
    print(f"{filepath} - {file_hashes[filepath]}")
