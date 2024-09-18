# Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2
# lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

def counter(vec) :
    occurrence_vector = {}

    for item in vec :
        if item not in occurrence_vector :
            occurrence_vector[item] = 1
        else:
            occurrence_vector[item] += 1
    return occurrence_vector

def item_appearing_x_time(x, *lists) :

    flattened_list = [item for sublist in lists for item in sublist]

    occurrence_vector = counter(flattened_list)

    elements = list(filter(lambda index : occurrence_vector[index] == x, occurrence_vector))

    return elements


if __name__ == "__main__" :
    list1 = [1, 2, 2, 3]
    list2 = [2, 1, 4, 5]
    list3 = [1, 2, 6, 1]
    x = 4

    print(item_appearing_x_time(x, list1, list2, list3))