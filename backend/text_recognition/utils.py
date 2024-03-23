from .models import Text


def remove_punctuation(text):
    text_lower_split_without_punctuation = text.replace(
        '.', '').replace(',', '').split()
    return text_lower_split_without_punctuation


def count_words(words):
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def create_list_from_dict(word_dict: dict):
    word_list = []

    for word, props in word_dict.items():
        text_obj = Text(word=word, term_frequency=props)
        word_list.append(text_obj)

    return word_list
