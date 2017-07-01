# Objective 
# In this challenge, we learn about Poisson distributions. Check out the Tutorial tab for learning materials!

# Task 
# A random variable, , follows Poisson distribution with mean of . Find the probability with which the random variable  is equal to .

# Input Format

# The first line contains 's mean. The second line contains the value we want the probability for:

# 2.5
# 5
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).

import math
lam = 2.5 # mean
k = 5
pr = lam**k * math.exp(-lam) / math.factorial(k)
print round(pr, 3)