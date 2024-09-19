# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Mackenzie Nguyen
# Date:2024-09-17
# Purpose: Create a variable, check its type and use a condition to check the value fo the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file

x = input("Enter a number: ")
print(type(x))
x = int(x);
if x >= 6:
    print("x is greater then 6!")

if x >= 4 or x < 2:
    print("x is greater than or equal to 4 or less than 2!")

