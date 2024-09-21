# .Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)

def operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    result = list()
    result.append(set1.intersection(set2))
    result.append(set1.union(set2))
    result.append(set1.difference(set2))
    result.append(set2.difference(set1))

    return result


if __name__ == "__main__":
    first_list = list(input("Enter first list (separated by spaces): ").split())
    second_list = list(input("Enter secod list (separated by spaces): ").split())

    print(operations(first_list, second_list))