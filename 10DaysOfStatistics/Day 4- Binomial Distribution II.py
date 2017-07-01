# Objective 
# In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

# Task 
# A manufacturer of metal pistons finds that, on average,  of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of  pistons will contain:

# No more than  rejects?
# At least  rejects?
# Input Format

# A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):

# 12 10
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print the answer to each question on its own line:

# The first line should contain the probability that a batch of  pistons will contain no more than rejects.
# The second line should contain the probability that a batch of  pistons will contain at least rejects.
# Round both of your answers to a scale of  decimal places (i.e.,  format).

import math
p = 0.12
q = 1-p
n = 10
x_all = 2
pr = 0
for x in range(x_all+1):
	pr += (math.factorial(n)/math.factorial(x)/math.factorial(n-x)) * p**x * q**(n-x)
print round(pr, 3)

pr = 0
for x in range(x_all, n+1):
	pr += (math.factorial(n)/math.factorial(x)/math.factorial(n-x)) * p**x * q**(n-x)
print round(pr, 3)