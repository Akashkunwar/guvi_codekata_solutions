# QID: 663
# 
# You are given with a queue. Your task is to reverse the queue elements and print it.
# 
# You are given a number ‘n’,denoting size of queue,
# Next line contains s space separated numbers
# 
# 
# 
# Print the reversed queue.
# 
# Sample Input : 
# 6
# 1 2 3 4 5 6
# 
# 
# Sample Output : 
# 6 5 4 3 2 1
# 


# Solution:


a = input()
a1 = [int(i) for i in input().split(" ")]
print(*a1[::-1], sep = " ")