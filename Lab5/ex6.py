# Write a function that receives a list with integers as parameter that contains an equal number
# of even and odd numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements)
# of numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
#
# Example:
#
# my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]

def make_pairs(lst):
    try:
        even_numbers = [element for element in lst if element%2 == 0]
        odd_numbers = [element for element in lst if element % 2 != 0]
        if len(even_numbers) != len(odd_numbers):
            raise ValueError("The list must to have an equal number of even and odd numbers.")
        even_dict = {index:element for index, element in enumerate(even_numbers)}
        odd_dict = {index:element for index, element in enumerate(odd_numbers)}
        size = len(even_numbers)
        result = []
        for index in range(0, size):
            result.append((even_dict[index], odd_dict[index]))
        return result
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    print(make_pairs([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

