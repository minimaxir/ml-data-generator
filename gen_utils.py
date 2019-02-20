import numpy as np
from collections import Counter

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

cat2_dict = {
    'a': 1,
    'b': 4,
    'c': 15
}


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
    return cat1_dict[key]


def cat2_transform(key):
    return cat2_dict[key]


def datetime2_transform(datetime_col):
    hour = datetime_col.dt.hour
    dayofweek = datetime_col.dt.dayofweek
    year = datetime_col.dt.year

    hour_tf = np.array([0.1 if x <= 6 or x >= 20 else 0.3 for x in hour])
    dayofweek_tf = np.array([0.2 if x >= 5 else 0.5 for x in dayofweek])
    year_tf = np.array([0.2 if x == 2017 else 0.5 for x in year])

    return hour_tf + dayofweek_tf + year_tf
