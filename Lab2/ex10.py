# Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc.
# Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

# Note: If input lists do not have the same number of items,
# missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.

def combine_lists(*lists) :
    maximum_length = max(len(lst) for lst in lists)
    new_lists = [lst + [None] * (maximum_length - len(lst)) for lst in lists]
    result = list(zip(*new_lists))
    return result

if __name__ == "__main__":
    print(combine_lists([1,2,3,6, 6], [5,6,7], ["a", "b", "c"]))