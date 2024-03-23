def count_words(text):
    # Приведение текста к нижнему регистру и разделение на слова
    words = text.lower().replace('.', '').split()

    # Создание словаря для подсчета вхождений слов
    word_count = {}

    # Подсчет встреч каждого слова
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Пример текста для анализа
text = "Сегодняшний день был особенно ярким и прекрасным."

# Подсчет встреч каждого слова в тексте
result = count_words(text)
x = 0
# Вывод результатов
for word, count in result.items():
    print(f"{word}: {count}")
    x += count
    print(x)
