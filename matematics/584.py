# QID: 584
# 
# Rohan is teacher at &ldquo;Sunsdfghpol&rdquo; academy about dfg numbers.Assume you are student of his coaching batch .He has given you some task.Your task is to print nth dfg  number.A dfg number is a number whose prime factors are only 2,3 or 5.
# 
# You are given a number ‘n’.
# 
# 
# Print all the dfg numbers upto index ‘n’.
# 
# 
# Sample Input : 
# 2
# 
# 
# Sample Output : 
# 1 2
# 


# Solution:


num = int(input())
arr = [1]
i = 0
while (len(arr) != num):
    i += 1
    if i%2 == 0 or i % 3 == 0 or i % 5 == 0:
        arr.append(i)
print(*arr)