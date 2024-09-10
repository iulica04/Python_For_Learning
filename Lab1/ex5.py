# Write a function that validates if a number is a palindrome.
from audioop import reverse

if __name__ == "__main__":

    number = input("Enter a number to test if it's a palindrome : ")
    prefix = number[:len(number)//2]
    r_prefix = prefix[::-1]
    result = number.endswith(r_prefix)

    if result :
        print("The number is a palindrome.")
    else:
        print("The number isn't a palindrome.")
