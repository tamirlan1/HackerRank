# Objective 
# In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

# Task 
# The ratio of boys to girls for babies born in Russia is . If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?

# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).

# Input Format

# A single line containing the following values:

# 1.09 1
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
p = 1.09/2.09
q = 1-p
n = 6
x_all = 3
pr = 0
for x in range(x_all, n+1):
	
	pr += (math.factorial(n)/math.factorial(x)/math.factorial(n-x)) * p**x * q**(n-x)

print round(pr, 3)