# Create a function and an anonymous function that receive a variable number of arguments.
# Both will return the sum of the values of the keyword arguments.
#
# Example:
#
# For the call my_function(1, 2, c=3, d=4) the returned value will be 7.

def my_function(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

if __name__ == "__main__":

    # real function
    print(my_function(6, x=1, y=5))

    #anonymous function
    my_anonymous_function =  lambda *args, **kwargs: sum(args) + sum(kwargs.values())

    print(my_anonymous_function(6, x=1, y=5))