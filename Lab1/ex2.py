# Write a script that calculates how many vowels are in a string.

def count_vowels(str):
    vowels = "aeiouAEIOU"
    count = 0

    for char in str:
        if char in vowels :
            count += 1

    return count

if __name__ == '__main__':

    str = input("Enter a string: ")

    print("The number of vowels for the input string %s is: %d" % (str, count_vowels(str)))
