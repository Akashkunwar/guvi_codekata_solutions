# QID: 545
# 
# A zx number is a number which is formed from the sum of 3 numbers ,and the three numbers are such that their hcf equal to 1.
# 
# You are given a number.You have to tell whether the number is zx or not,if yes then print the three numbers else 0
# 
# You are given a number ‘n’
# 
# 
# Print the three numbers if n is ‘zx’ number in ascending order else 0
# 
# 
# Sample Input : 
# 7
# 
# 
# Sample Output : 
# 2 3 2
# 


# Solution:


a = int(input())
prime = []
# Part 1
for i in range(2, a+1):
    for j in range(2, i):
        if i % j == 0:
            break 
    else:
        prime.append(i)
ans = []
rem = []
s = 0
for i in prime:
    s += i 
    if s <= a:
        ans.append(i)
    else:
        s -= i 
        if abs(a-s) in prime:
            ans.append(abs(a-s))
            break 
if len(ans) == 3:
    print(*ans)
else:
    ans = []
    for i in prime:
        x = i*3 
        if x == a:
            ans = [i for j in range(3)]
            break 
    if len(ans) == 3:
        print(*ans)
    else:
        print(0)