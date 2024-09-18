# Write a function to return a list of the first n numbers in the Fibonacci string.
# Fibonacci string : 0   1  1  2  3  5
#                    f0 f1 f2 f3 f4 f5 ..... fn = fn-2 + fn-1

def create_fibonacci_string(n) :
    fib_seq = [0, 1]

    for index in range(2, n) :
        next_fib_element = fib_seq[index-1] + fib_seq[index-2]
        fib_seq.append(next_fib_element)

    return fib_seq


if __name__ == "__main__" :
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print("The list of the first n numbers in the Fibonacci string: %s" % create_fibonacci_string(n))
