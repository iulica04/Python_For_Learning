# Write a module named app.py.
# When this module is run, it will run in an infinite loop, waiting for inputs from the user.
# The program will convert the input to a number and process it using the function process_item implemented in utils.py.
# You will have to import this function in your module. The program stops when the user enters the message "q".

import utils
from Lab5.ex1.utils import process_item

if __name__ == "__main__":
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting the program....")
            break

        try:
            x = int(user_input)
            print(f"The least prime number greater than {x} is {process_item(x)}.")
        except ValueError:
            print("Please enter a valid integer.")

