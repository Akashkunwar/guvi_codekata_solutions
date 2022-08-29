# QID: 627
# 
#  Rajat is given some special task to calculate the largest sum of two consecutive elements.He solved some of questions but he is not sure whether his answer is correct or not. Your task is to help him in determining whether answers posted by him are correct or not.
# 
# The first line of the input is a integer N. The second line of the input consists of N space separated integer.
# 
# 
# Print the max sum of two consecutive numbers from the given N numbers
# 
# 
# Sample Input : 
# 5
# 1 5 6 8 3
# 
# 
# Sample Output : 
# 14
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
b = []
for x in range(0,len(a)):
  try:
    b.append(a[x]+a[x+1])
  except:
    pass
print(max(b))