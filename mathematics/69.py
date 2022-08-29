# QID: 69
# 
# Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
# Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
# 
# 
# Sample Testcase :
# INPUT
# 2 5
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


lower,upper = map(int, input().split(" "))
count = 0
for num in range (lower, upper+1):
 if num>1:
  for i in range (2,num):
   if num % i==0:
    break
  else: 
    count += 1
print (count)