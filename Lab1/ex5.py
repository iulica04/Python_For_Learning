# Write a function that validates if a number is a palindrome.

def is_palindrome(number):
    prefix = number[:len(number) // 2]
    r_prefix = prefix[::-1]
    result = number.endswith(r_prefix)

    return result

if __name__ == "__main__":

    number = input("Enter a number to test if it's a palindrome : ")

    result = is_palindrome(number)

    if result :
        print("The number is a palindrome.")
    else:
        print("The number isn't a palindrome.")
