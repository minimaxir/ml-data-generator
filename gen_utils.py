import numpy as np
from collections import Counter


def text1_transform(text):
    text_split = text.split(" ")
    num_words = len(text_split)

    total = 0
    for i, word in enumerate(text_split):
        total += np.power(len(word), 1 + i / 100) / num_words

    return total


def text2_transform(text):
    counts = Counter(text)
    return sum([counts.get(x, 0) for x in 'aeiou'])


def cat1_transform(key):

    cat1_dict = {
        1: 2,
        2: -1,
        3: 4,
        4: 6,
        5: -6,
        6: 4,
        7: 9,
        8: 10,
        9: -4,
        10: 0
    }
    return cat1_dict[key]


def cat2_transform(key):

    cat2_dict = {
        'a': 1,
        'b': 4,
        'c': 15
    }
    return cat2_dict[key]
