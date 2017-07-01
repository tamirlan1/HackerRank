# Objective 
# In this challenge, we go further with Poisson distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

# Task 
# The manager of a industrial plant is planning to buy a machine of either type or type . For each day's operation:

# The number of repairs, , that machine  needs is a Poisson random variable with mean . The daily cost of operating  is .
# The number of repairs, , that machine  needs is a Poisson random variable with mean . The daily cost of operating  is .
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

# Input Format

# A single line comprised of  space-separated values denoting the respective means for  and :

# 0.88 1.55
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# There are two lines of output. Your answers must be rounded to a scale of  decimal places (i.e.,  format):

# On the first line, print the expected daily cost of machine .
# On the second line, print the expected daily cost of machine .

import math
lam1 = 0.88 # mean
lam2 = 1.55

# var(x) = E[x^2] - (E[x])^2
# E[x^2] = var(x) + (E[x])^2
# E[x^2] = lambda + lambda^2

expected_ca = 160 + 40*(lam1 + lam1**2)
expected_cb = 128 + 40*(lam2 + lam2**2)

print round(expected_ca, 3)
print round(expected_cb, 3)

