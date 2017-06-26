# In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

# Task 
# The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).

# Given an array, , of  integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each  occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e.,  format).

# Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

# Input Format

# The first line contains an integer, , denoting the number of elements in arrays  and . 
# The second line contains  space-separated integers describing the respective elements of array . 
# The third line contains  space-separated integers describing the respective elements of array .

# Constraints

# , where  is the  element of array .
# , where  is the  element of array .
# The number of elements in  is equal to .
# Output Format

# Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of decimal place (i.e.,  format).

# Sample Input

# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5
# Sample Output

# 9.0
# Explanation

# The given data is:

# InterquartileRange

# First, we create data set  containing the data from set  at the respective frequencies specified by : 
# As there are an even number of data points in the original ordered data set, we will split this data set exactly in half:# Enter your code here. Read input from STDIN. Print output to STDOUT

n = 6
num1 = [int(i) for i in '6 12 8 10 20 16'.split()]
freq = [int(i) for i in '5 4 3 2 1 5'.split()]
full = []
for i, val in enumerate(num1):
    full.extend(freq[i]*[val])

full = sorted(full)
n = len(full)
lower = full[:n/2]

if n%2==1:    
    upper = full[(n/2+1):]
else:
    upper = full[n/2:]
    
def median(l):
    n = len(l)
    if n%2 == 1:
        return l[n/2]
    else:
        return (l[n/2-1] + l[n/2]) / 2

print round((median(upper) - median(lower)), 1)