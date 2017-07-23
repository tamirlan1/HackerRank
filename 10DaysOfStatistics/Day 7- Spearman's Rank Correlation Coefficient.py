# Objective 
# In this challenge, we practice calculating Spearman's rank correlation coefficient. Check out the Tutorial tab for learning materials!

# Task
# Given two -element data sets,  and , calculate the value of Spearman's rank correlation coefficient.

# Input Format

# The first line contains an integer, , denoting the number of values in data sets  and . 
# The second line contains  space-separated real numbers (scaled to at most one decimal place) denoting data set . 
# The third line contains  space-separated real numbers (scaled to at most one decimal place) denoting data set .

# Constraints

# , where  is the  value of data set .
# , where  is the  value of data set .
# Data set  contains unique values.
# Data set  contains unique values.
# Output Format

# Print the value of the Spearman's rank correlation coefficient, rounded to a scale of  decimal places.

# Sample Input

# 10
# 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
# 200 44 32 24 22 17 15 12 8 4
# Sample Output

# 0.903
# Explanation

# We know that data sets  and  both contain unique values, so the rank of each value in each data set is unique. Because of this property, we can use the following formula to calculate the value of Spearman's rank correlation coefficient:

# Here,  is the difference between ranks of each pair . The following table shows the calculation of :


# Now, we find the value of the coefficient:

# When rounded to a scale of three decimal places, we get  as our final answer.

import math

n = int('10')
x = [float(i) for i in '10 9.8 8 7.8 7.7 1.7 6 5 1.4 2'.split()]
y = [int(i) for i in '200 44 32 24 22 17 15 12 8 4'.split()]

rankx = [sorted(x).index(v) + 1 for v in x]
ranky = [sorted(y).index(v) + 1 for v in y]

# if sorted(x) == sorted(set(x)):
rxy = 1 - 6*(sum([(i[0]-i[1])**2 for i in zip(rankx, ranky)]))*1.0 / (n*(n**2 - 1))
# else:
# 	mux = sum(rankx) * 1.0 / n
# 	sigx = math.sqrt(sum([(i-mux)**2 for i in rankx]) / n)
# 	muy = sum(ranky) * 1.0 / n
# 	sigy = math.sqrt(sum([(i-muy)**2 for i in ranky]) / n)
# 	# print rankx, ranky
# 	# print mux, sigx, muy, sigy
# 	rxy = sum([(i[0] - mux)*(i[1] - muy) for i in zip(x,y)]) / n / sigx / sigy

print round(rxy, 3)
