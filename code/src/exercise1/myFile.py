from os.path import abspath
import string


def read_in(file_path):
    file_path = abspath("../../../" + file_path)
    file = open(file_path, "r")
    return file.read()


def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

text = read_in("books/the_raven.txt")
#print(text)

text = remove_punctuation(text)
print(text)