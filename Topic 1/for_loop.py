"""
Program: for_loop.py
Author: Andy Volesky
Last date modified: 09/28/2021

The purpose of this program:

write a Python script (.py file)
Declare a list of floating point numbers
Write a for loop to print each
Write a second for loop to print the odd number descending from 99 to 33 (including 99 and 33)
Include in .py file a docstring.
"""

# list of floats
float_list = [5.0, 6.0, 7.0, 9.0, 1.0]

# looping through list and printing result
for num in float_list:
    print(num)

# setting range 99 to 33 and decrementing by 2 to get the odds.
for num in range(99,33,-2):
    print(num)