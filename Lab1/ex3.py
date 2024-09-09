# rite a script that receives two strings and prints the number of occurrences of the first string in the second.


def count_occurrences(str, substr):
    return str.count(substr);

if __name__ == "__main__":

    first_string = input("Enter a string: ")
    second_string = input("Enter another string: ")


    print("The number oof occurrences of the %s in %s is: %d" % (first_string, second_string, count_occurrences(first_string, second_string)))

