# QID: 607
# 
# Ramesh is given a special series to print,as he has some other work to do.Help ramesh in printing the series.
# 
#  
# 
# Note:Observe the series very keenly in examples
# 
# You are given a number ‘n’.
# 
# 
# Print the n term of series.
# 
# Sample Input : 
# 6
# 
# Sample Output : 
# 1 6 120
# 


# Solution:


a = int(input())
arr = list(range(1,a+1))
c = ['1']
d = int(len(arr)/3)
for i in range(d):
    r = 1
    for j in arr[(i*3):3+(i*3)]:
        r = r * j 
    c.append(r)
print(*c)