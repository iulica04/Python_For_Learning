# Write a function called process that receives a variable number of keyword arguments
# The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
# If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument
# and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
# If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
# If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list.
# The function will return the processed numbers.

# Example:
#
# def sum_digits(x):
#
#     return sum(map(int, str(x)))
#
# process(
#
#     filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
#
#     limit=2,
#
#     offset=2
#
# ) returns [34, 144]
#
# Explanation:

# Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

# Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040

# After offset: 34, 144, 610, 2584, 10946, 832040

# After limit: 34, 144

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def process(**kwargs):
    fib_sequence = generate_fibonacci(1000)

    filters = kwargs.get("filters", None)
    limit = kwargs.get("limit", None)
    offset = kwargs.get("offset", None)

    if filters is not None:
        for flt in filters:
            fib_sequence=list(filter(flt, fib_sequence))
    if offset is not None:
        fib_sequence = fib_sequence[offset:]
    if limit is not None:
        fib_sequence = fib_sequence[:limit]

    return fib_sequence

if __name__ == "__main__":
    #print(process(filters=[lambda item: item % 2 == 0]))
    print(process(filters=[lambda item: item % 2 == 0], offset=2, limit=3))


