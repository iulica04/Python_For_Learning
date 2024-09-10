# Write a functions that determine the most common letter in a string.
# For example if the string is "an apple is not a tomato",
# then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

def most_common_character(frequency) :
    maximum = -1
    common_letter = ""
    for key, value in frequency.items() :
        if value > maximum :
            maximum = value
            common_letter = key

    return common_letter


def count_letter(text) :
    frequency = {}
    for char in text :
        if char.isalpha() :
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return most_common_character(frequency)

if __name__ == "__main__" :
    input = input("Enter a text: ")

    print("The most common character in '%s' is: %s." % (input, count_letter(input)))
