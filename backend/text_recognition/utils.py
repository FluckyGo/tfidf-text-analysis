from math import log

from .models import Text, Document


def remove_punctuation(text):
    text_lower_split_without_punctuation = text.lower().replace(
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


def create_list_from_dict(word_dict: dict, doc_name):
    word_list = []

    for word, props in word_dict.items():
        text_obj = Text(word=word, word_quantity=props, doc_name=doc_name)
        word_list.append(text_obj)
    return word_list


def calculate_idf(word):
    total_documents = Document.objects.count()
    word_occurrences = Text.objects.filter(
        word=word).values('doc_name').distinct().count()
    if word_occurrences > 0:
        idf = log(total_documents / word_occurrences)
    else:
        idf = 0
    return idf
