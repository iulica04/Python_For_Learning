# Write a function that receives a string as a parameter and returns a dictionary in which the keys
# are the characters in the character string and the values are the number of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .


def counter(string):
    result = {}

    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result

if __name__ == "__main__":
    word = input("Enter a string: ")
    print(counter(word))