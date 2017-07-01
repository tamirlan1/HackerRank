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
p = 1.0/3 #defective
q = 1-p
n_all = 5
pr = 0
for n in range(1,n_all+1):
	pr += q**(n-1) * p
print round(pr, 3)