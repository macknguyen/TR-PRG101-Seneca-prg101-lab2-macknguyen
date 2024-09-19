# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Mackenzie Nguyen
# Date:2024-09-17
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2f.py

# TO DO 1: create the required variables and get thier values form users, convert the variables to int.
income = input("Enter your income: ")
status = input("Are you married or single: ")
income = int(income)
status = str(status)

# TO DO 2: write nested conditional statements to calcualte tax
if income > 32000 and status == ("single"):
    income = income - (3200 + (income * 0.25))
elif income >= 32000 and status == ("single"):
    income = income - (income  * 0.10)
elif income > 64000 and status == ("married"):
    income = income - (6400 + (income * 0.25))
else:
    income = income - (income * 0.10)

print ('Your {} and income after tax is {}'.format(status, income ))