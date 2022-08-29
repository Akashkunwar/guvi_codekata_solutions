# QID: 505
# 
# Loki wants to steal the tesseract but in order to do so, he has to rearrange the elements in an array in a specific manner which is mentioned in a clue. The clue says cursed are the odd and sorted are the even. Loki manages to decode the clue which translates to &ldquo;sort the even positioned elements of an array, starting from the element at index 0, in ascending order&rdquo;. Manipulate the array so as to help Loki steal the tesseract.
# 
#  
# 
# Size of the array followed by the elements of the array
# 
# 
# Even index array elements sorted in ascending order
# 
# 
# Sample Input : 
# 5
# 3 9 1 44 6
# 
# 
# Sample Output : 
# 1 9 3 44 6
# 
# 


# Solution:


a = int(input())
arr = list(map(int, input().split()))
odd = []
even = []
arr1 = []
for i in range(a):
    if i % 2 == 0 or i == 0:
        even.append(arr[i])
    elif i != 0 and i % 2 != 0:
        odd.append(arr[i])
even.sort()
for i in range(len(even)):
    arr1.append(even[i])
    if i < len(odd):
        arr1.append(odd[i])
print(*arr1)