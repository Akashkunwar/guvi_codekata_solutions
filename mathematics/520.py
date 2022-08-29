# QID: 520
# 
# Simi is learning about palindromic numbers. Her teacher gave him the task to count all palindromic numbers present in that range.Simi has told you about this and want your help. You design an algorithm in order to help simi.
# 
# You will be given a number ‘n’
# 
# 
# Print the count of all palindromic numbers till ‘n’(inclusive)
# 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 5
# 


# Solution:


n = int(input())
count = 0
for i in range(1, n+1):
    i = str(i)
    if i == i[::-1]:
        count += 1
print(count)