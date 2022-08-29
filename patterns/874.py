# QID: 874
# 
# Generate a  full pyramid using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the full pyramid using numbers based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     1
#    232
#   34543
#  4567654
# 567898765
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        l = []
        for j in range(i, (2*i)):
            l.append(str(j))
        for j in range((2*i)-2, i-1, -1):
            l.append(str(j))
        print(''.join(l))
        
n = int(input())
pattern(n)