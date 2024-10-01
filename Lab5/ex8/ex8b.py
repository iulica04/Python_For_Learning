#Write a function called multiply_output with one parameter named function.
# The function will return one new function which returns the output of the function received multiplied by 2.

def multiply_by_three(x):

    return x * 3

# augmented_multiply_by_three = multiply_output(multiply_by_three)
# x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)

def multiply_output(function):
    def new_function(*args, **kwargs):
        if len(args) > 1 and len(kwargs) != 0:
            raise TypeError(f"Function {function.__name__} expected 1 argument, got {len(args) + len(kwargs)}.")
        return function(*args, **kwargs) * 2

    return new_function

if __name__ == "__main__":
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10, 2)  # this will return 2 * (10 * 3)
    print(x)