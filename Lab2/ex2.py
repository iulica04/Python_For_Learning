#  Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

if __name__ == "__main__" :
    seq =  list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    prime_numbers = list(filter(lambda element : element > 1 and all(element % d == 0 for d in range(2, element//2+1)), seq))
    # we use all(...) because all() checks if every single condition (element % d != 0) is True for all d in the range.
    #If you don’t use all(), you would just be checking one condition at a time,
    # and that wouldn’t help us determine if the number is divisible by any number in the range.

    print(prime_numbers)