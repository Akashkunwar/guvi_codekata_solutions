
# You are given a long string without spaces.Your task is to place the vowels in ascending order. Then print the resulting string

# Input Description:
# You are given a string ‘s’

# Output Description:
# Print the obtained string

# Sample Input :
# ebcda

# Sample Output :
# abcde


# Solution

a = input()
a = list(a)

b = {}
for x in a:
  if x == 'a' or x =='e' or x =='i' or x =='o' or x == 'u':
    b[x] = a.index(x)

v = ['a','e','i','o','u']
c = list(b.keys())
d = list(b.values())
e = 0
for x in v:
  if x in c:
    a[d[e]] = x
    e = e+1
print(*a, sep='')