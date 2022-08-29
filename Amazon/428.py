# QID: 428
# 
# Mr. Kanga had a PhD in Heap Algorithms. Today, he was given a list of strings in random order. Help him sort the list in increasing order(lexicographically increasing) using heap sort.
# 
# The first line is an integer N denoting the number of strings.
# The next line contains N space separated strings containing lower case English Alphabets.
# 
# Print N space separated strings in increasing order.
# 
# Sample Input : 
# 2
# bag axe
# 
# Sample Output : 
# axe bag
# 


# Solution:


aa = input()
a = [str(i) for i in input().split(" ")]
a.sort()
print(*a)