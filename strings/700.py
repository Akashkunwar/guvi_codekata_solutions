# QID: 700
# 
# In a school there are voting to choose the monitor of class.Your task is to tell which candidate is winner and if there is a tie print the name of candidate whose come first in lexicographical order.
# 
# You are given with the space separated names.
# 
# 
# Print the winner’s name and the votes he earned.
# 
# 
# Sample Input : 
# john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john
# 
# 
# Sample Output : 
# john 4
# 
# 


# Solution:


from collections import Counter
a1 = [str(i) for i in input().split(" ")]
b = Counter(a1)
print(list(b.keys())[0],list(b.values())[0])