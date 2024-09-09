
def gcd(a, b) :
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    # Read input numbers from the console
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    result = numbers[0]
    for index in range(1, len(numbers)) :
        result = gcd(result, numbers[index])

    print(result)
