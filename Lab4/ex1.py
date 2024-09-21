# Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
#
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor
# din directorul dat ca parametru.
#
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’

import os
from os import listdir


def find_extensions(directory):
    if not os.path.isdir(directory):
        print("This path is not a directory.")
        return None

    elements_from_directory = listdir(directory)
    if not elements_from_directory :
        print("This directory is empty.")
    extensions = []

    for element in elements_from_directory:
        full_path_for_file = os.path.join(directory, element)
        if os.path.isfile(full_path_for_file):
            _, extension = os.path.splitext(element)
            extensions.append(extension.lstrip('.'))

    return sorted(extensions)

if __name__ == "__main__":
    print(find_extensions("D:\\Facultate 2.2\\SGBD"))