# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior,
# cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru,
# iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.

# Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
# returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel:
# dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv
# in toate fișierele din acel director.
# Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
import os

def search_in_files(file, to_search, callback):
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if to_search in line:
                    return True
            return False
    except FileNotFoundError:
        print_errors(f"The file at {file} was not found.")

def find_files_with_content(target, to_search, callback):
    try:
        if not os.path.exists(target):
            raise Exception("The path doesn't exists.")

        if os.path.isfile(target):
            if search_in_files(target, to_search, print_errors):
                return list(target)
        elif os.path.isdir(target):
            files_with_content = list()
            for root, dirs, files in os.walk(target):
                for file in files:
                    if search_in_files(os.path.join(root, file), to_search, print_errors):
                        files_with_content.append(file)
            return files_with_content
        else:
            raise ValueError("The target isn't a directory or a file.")

    except Exception as e:
        print_errors(e)

def print_errors(error):
    print(f"Error: {error}")

if __name__ == "__main__":
    print(find_files_with_content("D:\\Facultate 3.1\\Python\\Lab4", "def", print_errors))