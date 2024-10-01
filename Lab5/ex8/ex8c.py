# Write a function called augment_function with two parameters named function and decorators.
# decorators will be a list of functions which will have the same signature as the previous
# functions (print_arguments, multiply_output). augment_function will create a new function which is augmented using
# all the functions in the decorators list.
#
# Example:
#
# def add_numbers(a, b):
#
#     return a + b
#
# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
#
# x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))

from ex8b import multiply_output
from ex8a import print_arguments

def add_numbers(a, b):
    return a + b

def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)
    return function

if __name__ == "__main__":
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    x = decorated_function(3, 4)
    print(x)