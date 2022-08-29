# QID: 538
# 
# You are provided with a number n. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.
# 
# You are given with a number n.
# 
# 
# Print Saturated if it is saturated else it is Unsaturated
# 
# 
# Sample Input : 
# 121
# 
# 
# Sample Output : 
# Saturated
# 
# 


# Solution:


n = input().strip()
n = set(n)
if len(n) <= 2:
    print("Saturated")
else:
    print("Unsaturated")