# re.findall()

# The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings. 
# Code

# >>> import re
# >>> re.findall(r'\w','http://www.hackerrank.com/')
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
# re.finditer()

# The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 
# Code

# >>> import re
# >>> re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
# >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
# Task 
# You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-). 
# Your task is to find all the substrings of  that contains  or more vowels. 
# Also, these substrings must lie in between  consonants and should contain vowels only.

# Note : 
# Vowels are defined as: AEIOU and aeiou. 
# Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

# Input Format

# A single line of input containing string .

# Constraints


# Output Format

# Print the matched substrings in their order of occurrence on separate lines. 
# If no match is found, print -1.

# Sample Input

# rabcdeefgyYhFjkIoomnpOeorteeeeet
# Sample Output

# ee
# Ioo
# Oeo
# eeeee
# Explanation

# ee is located between consonant  and . 
# Ioo is located between consonant  and . 
# Oeo is located between consonant  and . 
# eeeee is located between consonant  and .



import re
inp = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
m = re.findall('(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', inp)
if m:
	for i in m:
		print i
else:
	print -1

