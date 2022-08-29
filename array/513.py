# QID: 513
# 
# Iron Man wants to extract an infinity stone from a safe. The safe is protected by a password and Iron Man knows the clue to the password which is &ldquo;sum one and two when sorted they are true&rdquo;. Decode the clue from the test case and help Iron Man open the safe.
# 
#  
# 
# Size of the array followed by the elements of the array
# 
# 
# Sum of 2 specific elements in the array.
# 
# 
# Sample Input : 
# 5
# 9 8 3 2 1
# 
# Sample Output : 
# 3
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
a.sort()
print(a[0]+a[1])