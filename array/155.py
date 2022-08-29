# QID: 155
# 
# Given a number N and an array of N integers, predict if the product of all elements would be even or odd(actual multiplication may lead to overflows ai <= 100000000).If there is only one element present in the array print whether that number is odd or even.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 4
# 2 4 4 2
# OUTPUT
# even
# 
# 
# 
# 


# Solution:


a = input()
list1 = [int(i) for i in input().split(" ")] 
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
z = multiplyList(list1)
if len(list1)==1:
  if list1[0]%2==0:
    print("even")
  else:
    print("odd")
elif z%2==0:
    print("even")
else:
  print("odd")