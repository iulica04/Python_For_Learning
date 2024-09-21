# Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
# and will return the number of positional arguments whose values can be found among keyword arguments values.
#
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return return 3


def count_positional_in_keywords(*args, **kwargs):

    kwargs_values = set(kwargs.values())

    return sum(1 for arg in args if arg in kwargs_values)

if __name__ == "__main__":
    print(count_positional_in_keywords(1, 2, 3, 4, 3, x=1, y=2, z=3, w=5))