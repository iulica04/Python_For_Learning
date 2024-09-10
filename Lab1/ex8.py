# Write a function that counts how many bits with value 1 a number has. For example for number 24,
# the binary format is 00011000, meaning 2 bits with value "1"


def count_bit_1 (number):
    binary_number_string = str(bin(number)[2:])
    return binary_number_string.count("1")

if __name__ == "__main__" :
    decimal_number = int(input("Enter a decimal number: "))
    print("The binary form for number %d is %s and have %d bits with value '1'." % (decimal_number, bin(decimal_number), count_bit_1(decimal_number)))
