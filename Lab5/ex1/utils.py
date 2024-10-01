# Write a module named utils.py that contains one function called process_item.
# The function will have one parameter, x, and will return the least prime number greater than x.
# When run, the module will request an input from the user,
# convert it to a number and it will display the output of the process_item function.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number//2+1):
        if number % i == 0:
            return False
    return True

def process_item(x):
    number = x + 1
    while not is_prime(number):
        number += 1
    return number

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"The least prime number greater than {number} is: {process_item(number)}")

