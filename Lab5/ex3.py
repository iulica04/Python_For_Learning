# Using functions, anonymous functions, list comprehensions and filter,
# implement three methods to generate a list with all the vowels in a given string.
#
# For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

def get_vowels1(string):
    vowels = ['o', 'a', 'i', 'i', 'o', 'i', 'u']
    return list(filter(lambda char: char in vowels, string))

def get_vowels2(string):
    vowels = ['o', 'a', 'i', 'i', 'o', 'i', 'u']
    return [char for char in string if char in vowels]

def get_vowels3(string):
    vowels = ['o', 'a', 'i', 'i', 'o', 'i', 'u']
    vowels_of_string =[]
    for char in string:
        if char in vowels:
            vowels_of_string.append(char)

    return vowels_of_string

if __name__ == "__main__":
    print(get_vowels1("Programming in Python is fun"))
    print(get_vowels2("Programming in Python is fun"))
    print(get_vowels3("Programming in Python is fun"))
