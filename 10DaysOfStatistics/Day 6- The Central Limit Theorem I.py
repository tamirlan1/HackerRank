# Objective 
# In this challenge, we practice solving problems based on the Central Limit Theorem. Check out the Tutorial tab for learning materials!

# Task 
# A large elevator can transport a maximum of  pounds. Suppose a load of cargo containing  boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of pounds and a standard deviation of  pounds. Based on this information, what is the probability that all boxes can be safely loaded into the freight elevator and transported?

# Input Format

# There are  lines of input (shown below):

# 9800
# 49
# 205
# 15
# The first line contains the maximum weight the elevator can transport. The second line contains the number of boxes in the cargo. The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation.

# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print the probability that the elevator can successfully transport all  boxes, rounded to a scale of  decimal places (i.e.,  format).

import math
max_load = 9800
n = 49
mu = 205
sigma = 15

mu_tot = mu * n
sigma_tot = sigma * math.sqrt(n)

def cum(x, mu, sigma):
	phi = 0.5*(1 + math.erf( (x - mu) / (sigma * math.sqrt(2)) ) )
	return phi

print round(cum(max_load, mu_tot, sigma_tot), 4)