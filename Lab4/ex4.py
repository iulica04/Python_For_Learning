# Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument
# la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
#
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.

import os
from os import listdir


def unique_extensions(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise Exception("The path need to be a path for a directory.")
        extensions = set()
        elements = listdir(directory_path)
        for element in elements:
            element_path = os.path.join(directory_path, element)
            if os.path.isfile(element_path):
                _, extension = os.path.splitext(element)
                extensions.add(extension)

        extensions = list(extensions)
        return sorted(extensions)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(unique_extensions("D:\\Facultate 3.1\\Python\\Lab4"))