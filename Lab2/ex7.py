#  Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
#  The first element of the tuple will be the number of palindrome numbers found in  the list
#  and the second element will be the greatest palindrome number.
from Lab1.ex5 import is_palindrome

def process_palindromes(numbers) :
    list_of_palindrome_numbers = list()


    for number in numbers :
        if is_palindrome(str(number)) :     # because the imported function expects a parameter of type string
            list_of_palindrome_numbers.append(number)

    return len(list_of_palindrome_numbers), max(list_of_palindrome_numbers)


if __name__ == "__main__" :
    numbers = list(map(int, input("Enter a list of numbers(integers) separated by spaces: ").split()))

    print(process_palindromes(numbers))
