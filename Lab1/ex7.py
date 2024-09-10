# Write a script that converts a string of characters written in UpperCamelCase into
# lowercase_with_underscores.

def transform(text) :
    result = ""

    for index, char in enumerate(text) :
        if char.isupper() :
            if index != 0 :
                result += '_'
            result += char.lower()
        else :
            result += char

    return result


if __name__ == "__main__" :
    input = input("Enter a text in UpperCamelCase rule: ")
    print("The conversion of a string from UpperCamelCase into lower_with_underscores is : %s" % transform(input))

