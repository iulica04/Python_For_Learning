# Write a function that receives a list of pairs of integers (tuples with 2 elements)
# as parameter (named pairs). The function should return a list of dictionaries for each pair
# (in the same order as in the input list) that contain the following keys (as strings): sum (the value should be
# sum of the 2 numbers), prod (the value should be product of the two numbers), pow (the value should be the first number
# raised to the power of the second number)
#
# Example:
#
# f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] )
# will return
# [{'sum': 7, 'prod': 10, 'pow': 25},
# {'sum': 20, 'prod': 19, 'pow': 19},
# {'sum': 36, 'prod': 180, 'pow': 729000000},
# {'sum': 4, 'prod': 4, 'pow': 4}]

def make_operations(list_of_pairs):
    result = []
    for pair in list_of_pairs:
        number1 = pair[0]
        number2 = pair[1]

        dictionary = {'sum': number1 + number2,
                      'prod': number1 * number2,
                      'pow': number1 ** number2}
        result.append(dictionary)
    return result

if __name__ == "__main__":
    print(make_operations([(5, 2), (19, 1), (30, 6), (2, 2)]))


