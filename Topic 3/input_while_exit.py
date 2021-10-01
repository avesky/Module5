"""
Program: input_while_exit.py
Author: Andy Volesky
Last date modified: 09/29/2021

The purpose of this program:

Write a small script, input_while_exit.py
that prompts the user for numeric input between 1 and 100.
Prompt the user until the input is in the correct range. Once a the input is correct, store the input in a list.

add code to exit (aka break out of) the inner while if the user input a sentinel flag indicating
they no longer have input. Implement this option by adding the appropriate exit statement to the inner while loop.
Run the code.
Notice that the code does not exit the outer while loop. There are a few ways to fix the
code so it will exit this loop as well. Fix the code.
Add doctring to the top of your file, add comments at the bottom with your tests
and observed output after a few test runs of your code.
"""


# 1st part following pseudocode
# test_list = []
# user_number = int(input('Enter a number: '))
# while 1 > user_number or user_number > 100:
#    user_number = int(input('Enter a number: '))
# test_list.append(user_number)
# for num in test_list:
#    print(num)


# 2nd part following pseudocode
data_list = []

while True:
    user_input = input('Enter a number between 1 and 100 (999 to stop): ')
    if not user_input.isnumeric():
        print("that doesn't look like a number")
        continue
    user_number = int(user_input)
    if user_number == 999:
        print("detected sentinel value. exiting")
        print("here are the valid values you entered:")
        print(", ".join(map(str, data_list)))
        quit()
    if  1 <= user_number <= 100:
        data_list.append(user_number)
    else:
        print("invalid entry. please constrain your input to the range [1, 100]")


# tested numbers 2, 5, 8, 90, 999
# printed 2, 5, 8, 90

# tested numbers -3, -10, 500, 90, 7, -8, 50, 999
# printed 90, 7, 50

# tested 50, 98, 26, 65, 98, -8, 999
# printed 50, 98, 26, 65, 98  looks like we can exit out of the inner loop now.