# Write a function that extract a number from a text
# (for example if the text is "An apple is 123 USD", this function will return 123,
# or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.

def find_the_first_number(str):
    number = ''
    for char in str :
        if char.isdigit() :
            number += char
        elif number :
            break

    return number


if __name__ == "__main__" :
    input = input("Enter the text : ")
    print("The first number that was found in your chosen text is : %s." % find_the_first_number(input))

