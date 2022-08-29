# QID: 915
# 
# Write a code to generate a aplhabet half pyramid pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=26.
# 
# Print the alphabet half pyramid pattern according to the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# EDCBA
# EDCB
# EDC
# ED
# E
# 


# Solution:


def pattern(n):
    let = 65
    for i in range(n):
        for j in range(n-1, i-1, -1):
            print(chr(let+j), end = "")
        print()
        
n = int(input())
pattern(n)