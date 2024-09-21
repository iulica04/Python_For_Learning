# Să se scrie o funcție ce primește ca parametru un string my_path.
#
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
# sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie.
# Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
import os


def filter_path(my_path):
    try:
        if not os.path.exists(my_path):
            raise Exception(f"Path: {my_path} does not exits.")

        if os.path.isfile(my_path):
            with open(my_path, 'r') as f:
                f.seek(0, 2)
                file_size = f.tell()

                if file_size < 20:
                    print(f"The file contains {file_size} characters, not 20.")
                    f.seek(file_size)
                else:
                    f.seek(file_size-20)

                return f.read()
        elif os.path.isdir(my_path):
            extensions = {}

            for root, dirs, files in os.walk(my_path):
                for file in files:
                    _, extension = os.path.splitext(file)
                    if extension in extensions:
                        extensions[extension] += 1
                    else:
                        extensions[extension] = 1

            return sorted(extensions.items(), key = lambda item : item[1], reverse = True)
        else:
            raise Exception("The path need to be a path for a file or for a directory.")


    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(filter_path("D:\\Facultate 3.1\\Python\\Lab4"))
