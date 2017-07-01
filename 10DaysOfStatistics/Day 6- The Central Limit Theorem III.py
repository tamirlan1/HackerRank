# Objective 
# In this challenge, we practice solving problems based on the Central Limit Theorem. We recommend reviewing the Central Limit Theorem Tutorial before attempting this challenge.

# Task 
# You have a sample of  values from a population with mean  and with standard deviation . Compute the interval that covers the middle  of the distribution of the sample mean; in other words, compute  and  such that . Use the value of . Note that  is the z-score.

# Input Format

# There are five lines of input (shown below):

# 100
# 500
# 80
# .95
# 1.96
# The first line contains the sample size. The second and third lines contain the respective mean () and standard deviation (). The fourth line contains the distribution percentage we want to cover (as a decimal), and the fifth line contains the value of .

# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print the following two lines of output, rounded to a scale of  decimal places (i.e.,  format):

# On the first line, print the value of .
# On the second line, print the value of .

import math
n = 100
mu = 500
sigma = 80
perc = 0.95
z = 1.96

mu_tot = mu * n
sigma_tot = sigma * math.sqrt(n)

a = (mu_tot - sigma_tot * z) / n
b = (mu_tot + sigma_tot * z) / n

print round(a, 2)
print round(b, 2)