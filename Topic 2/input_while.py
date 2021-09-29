"""
Program: input_while.py
Author: Andy Volesky
Last date modified: 09/28/2021

The purpose of this program:

Write a small script, input_while.py
that prompts the user for numeric input between 1 and 100.
Prompt the user until the input is in the correct range. Once a the input is correct, store the input in a list.
"""

"""
declare a list variable
prompt and get the user input
while user input is not good (in range)
     prompt user for good input
store in list
print the list
That's not useful! You need multiple inputs from the user,

declare a list variable
declare a sentinel value for user input
prompt get the user input (indicating sentinel value to stop)
while sentinel value is not stopping value 
      while user input is not good (in range)
            prompt user for good input
      store in list
      prompt and get the next user input

print the list using a for loop
 
Test running your script in the shell.
"""

# 1st part following pseudocode
#test_list = []
#user_number = int(input('Enter a number: '))
#while 1 > user_number or user_number > 100:
#    user_number = int(input('Enter a number: '))
#test_list.append(user_number)
#for num in test_list:
#    print(num)


# 2nd part following pseudocode
test_list = []
user_number = int(input('Enter a number between 1 and 100 (999 to stop): '))
while user_number != 999:
    while 1 > user_number or user_number > 100:
        user_number = int(input('Enter a good number please: '))
    test_list.append(user_number)
    user_number = int(input('Enter a number between 1 and 100 (999 to stop): '))
for num in test_list:
    print(num)


# tested numbers 2, 5, 8, 90, 999
# printed 2, 5, 8, 90

# tested numbers -3, -10, 500, 90, 7, -8, 50, 999
# printed 90, 7, 50