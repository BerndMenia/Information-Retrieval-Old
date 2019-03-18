from os.path import abspath

def read_in(file_path):
    file_path = abspath("../../../" + file_path)
    file = open(file_path, "r")
    return file.read()


string = read_in("books/the_raven.txt")
print(string)