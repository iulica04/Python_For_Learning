# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag
# is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
#
#  Example: x = 2, ["test", "hello", "lab002"], flag = False
#  will return (["e", "s"], ["e" . Note: The function must return list of lists.

def filter_strings(strings, x=1, flag =True) :
    result = []
    for string in strings :
        characters = []
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    characters.append(char)
            else:
                if ord(char) % x == 1:
                    characters.append(char)
        result.append(characters)

    return result



if __name__ == "__main__" :
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False

    print(filter_strings(strings, x, flag))