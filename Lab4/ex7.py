# Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către
# un fișer si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False daca se poate citi din/scrie in fisier.
import os
from os import O_RDONLY, O_WRONLY


def see_details(file_path):
    try:
        if not os.path.isfile(file_path):
            raise Exception(f"the element at path {file_path} isn't a file.")

        result = {}
        result["full_path"] = os.path.abspath(file_path)
        result["file_size"] = os.path.getsize(file_path)
        _, extension = os.path.splitext(file_path)
        result["file_extension"] = extension
        result["can_read"] = os.access(file_path, os.R_OK)
        result["cad_write"] = os.access(file_path, os.W_OK)

        return result
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(see_details("D:\\Facultate 3.1\\Python\\Lab4\\ex1.py"))

