# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Mackenzie Nguyen
# Date:2024-09-17
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

import sys

arguments = len(sys.argv)

if arguments < 3:
    print("The script requires at least 2 arguments.")
else:
    name = sys.argv[1]
    age = sys.argv[2]
    if arguments == 2:
    
        print(f"Hi {name}, you are {age} years old and the script received exactly 2 arguments!")
    else:
        print(f"Hi {name}, you are {age} years old and the script received {arguments - 1} arguments.")


