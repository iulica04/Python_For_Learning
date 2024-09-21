#  Write a function that receives as a parameter a list and returns a tuple (a, b),
#  representing the number of unique elements in the list, and b representing the number of duplicate elements in the list
#  (use sets to achieve this objective).

def count_unique_and_duplicates(numbers):
    count_of_all_numbers = len(numbers)
    count_of_unique_numbers = len(set(numbers))
    count_of_duplicate_numbers = count_of_all_numbers - count_of_unique_numbers

    return count_of_unique_numbers, count_of_duplicate_numbers


if __name__ == "__main__":
    print(count_unique_and_duplicates([1, 2, 3, 4, 5, 6, 1, 1, 1, 1,]))