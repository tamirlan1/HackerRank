# Objective 
# In this challenge, we learn about geometric distributions. Check out the Tutorial tab for learning materials!

# Task 
# The probability that a machine produces a defective product is . What is the probability that the defect is found during the  inspection?

# Input Format

# The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for:

# 1 3
# 5
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).

import math
p = 1.0/3 #defective
q = 1-p
n = 5
pr = q**(n-1) * p
print round(pr, 3)