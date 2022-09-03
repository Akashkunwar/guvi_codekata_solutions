

# You are given a number “N” and string ‘S’ of digits denoting a positive integer [ N < sizeof(S) ] , build the lowest number possible by removing N digits from S, without changing their order.

# Input Description:
# The first line contains a positive integer N. The second line contains a string of digits denoting a positive integer S.

# Output Description:
# Print the lowest number that is formed

# Sample Input :
# 4
# 1234567

# Sample Output :
# 123



# Solution 

a = int(input())
b = input()
l = len(b)
m = l-a
c = list(b)
c.sort()
d = c[:m]
d = ''.join(d)
d = int(d)
print(d)