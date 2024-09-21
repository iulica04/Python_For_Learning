# Să se scrie o funcție ce primește un parametru cu numele dir_path.
# Acest parametru reprezintă calea către un director aflat pe disc.
# Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
#
# Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
#
# Calea "C:\\director" are pe disc următoarea structură:
#
# C:\\director\\fisier1.txt <- fișier
#
# C:\\director\\fisier2.txt <- fișier
#
# C:\\director\\director1 <- director
#
# C:\\director\\director2 <- director

import os

def get_abs_paths(dir_path):
    try:
        if not os.path.isdir(dir_path):
            raise Exception("The provided path must must be a valid directory.")

        paths = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if root == dir_path:
                    full_path = os.path.join(root, file)
                    paths.append(full_path)
        return paths
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(get_abs_paths("D:\\Facultate 3.1\\Python\\Lab4"))