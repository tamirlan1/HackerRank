# Objective 
# In this challenge, we practice using linear regression techniques. Check out the Tutorial tab for learning materials!

# Task 
# A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, , and Statistics course grade, , can be expressed as the following list of  points:

# If a student scored an  on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of when .

# Input Format

# There are five lines of input; each line contains two space-separated integers describing a student's respective and  grades:

# 95 85
# 85 95
# 80 70
# 70 65
# 60 70
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).

import math

x = []
y = []
inps = [
'95 85',
'85 95',
'80 70',
'70 65',
'60 70',
]
for i in range(5):
	# inp = raw_input().split()
	inp = inps[i].split()
	x.append(int(inp[0]))
	y.append(int(inp[1]))

sumxy = sum([i[0]*i[1] for i in zip(x,y)])
sumx = sum(x)
sumy = sum(y)
sumx2 = sum([i**2 for i in x])
n = len(x)
b = (n*sumxy - sumx*sumy)*1.0 / (n*sumx2 - (sumx)**2)

mux = sumx / n
muy = sumy / n
a = muy - b*mux
x0 = 80
y0 = b*x0 + a
print round(y0, 3)

# from sklearn import linear_regression
