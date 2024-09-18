#  Write a function that receives as parameters two lists a and b and returns:
#  (a intersected with b, a reunited with b, a - b, b - a)

if __name__ == "__main__" :
    first_list = list(map(int, input("Enter a list of numbers separated by spaces named A: ").split()))
    second_list = list(map(int, input("Enter another list of numbers separated by spaces named B: ").split()))

    intersection = [element for element in  first_list if element in second_list]
    print("A intersected with B: %s" % intersection)

    a_minus_b = [element for element in first_list if element not in second_list]
    print("A - B: %s" % a_minus_b)

    b_minus_a = [element for element in second_list if element not in first_list]
    print("B - A: %s" % b_minus_a)

    reunion = a_minus_b.copy()
    reunion.extend(b_minus_a)
    reunion.extend(intersection)
    reunion.sort()

    print("A reunited with B: %s" % reunion)