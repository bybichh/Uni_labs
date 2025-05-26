# Функція підрахунку кількості кожного слова в тексті
def count_words(text):
    text = text.lower()  # Приводимо текст до нижнього регістру
    for char in "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~":  # Видаляємо розділові знаки
        text = text.replace(char, '')
    words = text.split()  # Розбиваємо текст на слова
    counts = {}  # Словник для збереження підрахунку
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # Збільшуємо лічильник слова
    return counts

# Вибір користувача: ввести свій текст чи використати стандартний
choice = input("Choise 0 to put your own text / press Enter to use default: ").strip()
if choice == "0":
    text = input("Enter yours text: ")  # Отримуємо текст від користувача
else:
    # Текст за замовчуванням
    text = (
        "The sun rises in the east and sets in the west. "
        "Every morning the light spreads across the sky, bringing warmth and life. "
        "Birds sing, flowers open, and the world begins to move again. "
        "The cycle repeats, day after day, in perfect harmony with time."
    )
    print(text)

# Отримуємо словник з підрахунком слів
word_counts = count_words(text)

# Список слів, що зустрічаються більше 3 разів
frequent = [word for word, count in word_counts.items() if count > 3]

# Виводимо результати
print("Word frequency dictionary:", word_counts)
print("Words appearing more than 3 times:", frequent)
