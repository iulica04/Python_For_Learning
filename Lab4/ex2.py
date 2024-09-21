# Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
#
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

import os
from os import listdir


def write_files_path(directory_path, file_path):
    try:
        if not os.path.isdir(directory_path):
            raise Exception(f"{directory_path} isn't a directory.")
        if not os.path.isfile(file_path):
            raise Exception(f"{file_path} isn't a file.")

        with open(file_path, "w") as f:
            directory_elements = listdir(directory_path)
            files_to_write = []
            for element in directory_elements:
                file = os.path.join(directory_path, element)
                if element.startswith("A"):
                    files_to_write.append(file + '\n')

            f.writelines(files_to_write)

        print("The writing to the file was successfully completed.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    write_files_path("D:\\Facultate 3.1\\Python\\Lab3", "D:\\Facultate 3.1\\Python\\Lab4\\directory_for_tests\\file_for_ex4.txt")