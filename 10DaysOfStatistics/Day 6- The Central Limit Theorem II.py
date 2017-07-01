# Objective 
# In this challenge, we practice solving problems based on the Central Limit Theorem. We recommend reviewing the Central Limit Theorem Tutorial before attempting this challenge.

# Task 
# The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of  and a standard deviation of .

# A few hours before the game starts,  eager students line up to purchase last-minute tickets. If there are only  tickets left, what is the probability that all  students will be able to purchase tickets?

# Input Format

# There are  lines of input (shown below):

# 250
# 100
# 2.4
# 2.0
# The first line contains the number of last-minute tickets available at the box office. The second line contains the number of students waiting to buy tickets. The third line contains the mean number of purchased tickets, and the fourth line contains the standard deviation.

# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print the probability that  students can successfully purchase the remaining  tickets, rounded to a scale of decimal places (i.e.,  format).

import math
max_tickets = 250
n = 100
mu = 2.4
sigma = 2.0

mu_tot = mu * n
sigma_tot = sigma * math.sqrt(n)

def cum(x, mu, sigma):
	phi = 0.5*(1 + math.erf( (x - mu) / (sigma * math.sqrt(2)) ) )
	return phi

print round(cum(max_tickets, mu_tot, sigma_tot), 4)