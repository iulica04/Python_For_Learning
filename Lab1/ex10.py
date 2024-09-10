# Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated by only ONE space.
# For example: "I have Python exam" has 4 words.

if __name__ == "__main__" :

    correct_text = False
    text = ""
    while not correct_text :
        text = input("Enter a text: ")
        if text.count(' ') != 0 :
            print("You entered a correct text!")
            correct_text = True
        else:
            print("You entered a wrong text. A text is considered to be form out of words that are separated by only ONE space.\n Try again!!")

    words = text.split(' ')
    filtered_list = [item for item in words if item != '']

    print("In the text you entered exists %d words." % len(filtered_list))