# QID: 122
# 
# Given an array of N elements switch(swap) the element with the adjacent element and print the output.
# 
# 
# Sample Testcase :
# INPUT
# 5
# 3 2 1 2 3
# OUTPUT
# 2 3 2 1 3
# 
# 
# 
# 


# Solution:


a = input()
data = [int(i) for i in input().split(" ")]
i = 0
while i < data.__len__() - 1:
    t = data[i]
    data[i] = data[i + 1]
    data[i + 1] = t
    i = i + 2
print(*data)