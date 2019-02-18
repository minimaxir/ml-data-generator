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
