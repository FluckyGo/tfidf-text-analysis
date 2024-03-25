from math import log
from typing import Literal

from .models import Text, Document


def remove_punctuation(text: str) -> list[str]:
    text_lower_split_without_punctuation: list[str] = text.lower().replace(
        '.', '').replace(',', '').split()
    return text_lower_split_without_punctuation


def count_words(words) -> dict:
    word_count: dict = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def create_list_from_dict(word_dict: dict, doc_name) -> list:
    word_list: list = []

    for word, props in word_dict.items():
        text_obj = Text(word=word, word_quantity=props, doc_name=doc_name)
        word_list.append(text_obj)
    return word_list


def calculate_idf(word) -> float | Literal[0]:
    total_documents: int = Document.objects.count()
    word_occurrences: int = Text.objects.filter(
        word=word).values('doc_name').distinct().count()
    if word_occurrences > 0:
        idf: float = log(total_documents / word_occurrences)
    else:
        idf = 0
    return idf
