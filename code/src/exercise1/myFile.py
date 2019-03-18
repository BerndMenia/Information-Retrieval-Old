from os.path import abspath
from collections import Counter

import string



# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# https://stackoverflow.com/questions/9427037/relative-path-not-working-even-with-init-py
def read_in(file_path):
    file_path = abspath("../../../" + file_path)
    file = open(file_path, "r")
    return file.read()


# https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))


def total_number_of_terms(s):
    return len(s.split())


def unique_terms(text=""):
    lst = []
    for s in text:
        if not s in lst:
            lst.append(s)
    return lst


# https://stackoverflow.com/questions/40985203/counting-letter-frequency-in-a-string-python
def calculate_frequency(s):
    counts = Counter(s)  # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
    counts.most_common()
    # for i in s:
    #     print(i, counts[i])
    return counts


text = read_in("books/the_raven.txt")
# print(text)

text = remove_punctuation(text)
# print(text)

print("Total number of terms:", total_number_of_terms(text))

text_split = text.split()
print("Total number of unique terms:", len(unique_terms(text_split)))

frequency = calculate_frequency(text_split)
print(frequency)
print(type(frequency))
