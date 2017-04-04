# re

# A regular expression (or RegEx) specifies a set of strings that matches it.

# A regex is a sequence of characters that defines a search pattern, mainly for the use of string pattern matching.


# The re.search() expression scans through a string looking for the first location where the regex pattern produces a match. 
# It either returns a MatchObject instance or returns None if no position in the string matches the pattern.

# Code

# >>> import re
# >>> print bool(re.search(r"ly","similarly"))
# True

# The re.match() expression only matches at the beginning of the string. 
# It either returns a MatchObject instance or returns None if the string does not match the pattern. 
# Code

# >>> import re
# >>> print bool(re.match(r"ly","similarly"))
# False
# >>> print bool(re.match(r"ly","ly should be in the beginning"))
# True
# Task 
# You are given a string . 
# Your task is to verify that  is a floating point number.

# In this task, a valid float number must satisfy all of the following requirements:

#  Number can start with +, - or . symbol. 
# For example: 
# ✔
# +4.50 
# ✔
# -1.0 
# ✔
# .5 
# ✔
# -.7 
# ✔
# +.4 
# ✖
#  -+4.5

#  Number must contain at least  decimal value. 
# For example: 
# ✖
#  12. 
# ✔
# 12.0  

#  Number must have exactly one . symbol. 
#  Number must not give any exceptions when converted using .

# Input Format

# The first line contains an integer , the number of test cases. 
# The next  line(s) contains a string .

# Constraints


# Output Format

# Output True or False for each test case.

# Sample Input

# 4  
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff
# Sample Output

# False
# True
# True
# False
# Explanation

# : O is not a digit. 
# : is valid. 
# : is valid. 
# SomeRandomStuff: is not a number.

import re
n = int(raw_input())

for i in range(n):
    num = raw_input()
    print bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', num))