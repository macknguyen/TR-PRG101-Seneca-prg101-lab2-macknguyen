
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Mackenzie Nguyen
# Date:2024-09-17
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.

str1 = input("Enter a sentance: ")
str2 = input("Enter another sentance: ")
(len(str1))
(len(str2))
if (len(str1)) == (len(str2)):
    print('"{}" and "{}" are of equal length!'.format(str1, str2))
elif (len(str1)) > (len(str2)):
    print('"{}" is longer than "{}"!'.format(str1,str2))
else:
    print('"{}" is longer than "{}"!'.format(str2,str1))



 