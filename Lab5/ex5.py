#  Write a function with one parameter which represents a list.
#  The function will return a new list containing all the numbers found in the given list.
#
# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]

def my_function(lst):
    result = set()
    for element in lst:
        if isinstance(element, list):
            numbers_in_list = my_function(element)
            result.union(numbers_in_list)
        elif isinstance(element, (tuple, set)):
            numbers_in_list = my_function(list(element))
            result.union(numbers_in_list)
        elif isinstance(element, dict):
            numbers_in_list = my_function(list(element.values()))
            result.union(numbers_in_list)
        elif isinstance(element, (int, float)):
            result.add(element)

    return list(result)

if __name__ == "__main__":
    print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))