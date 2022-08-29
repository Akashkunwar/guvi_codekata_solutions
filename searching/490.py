# QID: 490
# 
# Ria is always fascinated by the number 2. She always wants to know who came second in a race, the second person to set foot on the moon and so on. She is given a list of numbers and asked to find the maximum. As always, she reports the second highest number as the maximum because according to her, 2 is higher than 1. Find out which was the number that Ria would have reported, given a list of N numbers.
# 
#  
# 
# Size of the array followed by the elements of the array.
# 
# 
# Second largest element of the array.
# 
# 
# Sample Input : 
# 10
# 1 9 8 7 6 5 2 3 4 10
# 
# 
# Sample Output : 
# 9
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
a.sort()
print(a[-2])