# QID: 487
# 
# Jaspreet is a marketing manager and on inspecting the product ids of products documented as sold, he finds out that the sales person has repeated a few of the product ids. He decides to warn the sales person who has repeated the same product id thrice. Your task is to find out the number of triplets(ids occurring thrice) of product ids recorded.
# 
# Constraints:
# 
# 1 <= N <= 100
# 
# 1 <= A[] <= 1000
# 
#  
# 
# Number of product ids followed by the list of product ids
# 
# Number of triplets detected.
# 
# Sample Input : 
# 10
# 2 1 1 3 1 8 7 2 2 6 
# 
# 
# Sample Output : 
# 2
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
b = []
for x in a:
  b.append(a.count(x))

c = []
for x in range(3,10):
  c.append(b.count(x))

c=[x for x in c if x!=0]
print(len(c))