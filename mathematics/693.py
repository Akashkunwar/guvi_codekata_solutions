# QID: 693
# 
# You are head incharge of sports activity in queue. Your task is to sort the students height wise in line. But you can only swap students.Your task is to determine the minimum possible swaps required to sort the students in queue according to heights
# 
# You are given with number ‘n’ denoting number of students. Next line contains n space separated integers denoting their height.
# 
# 
# 
# Print the minimum number of swaps required to sort the students in line.
# 
# Sample Input : 
# 5
# 1 5 4 3 2
# 
# 
# Sample Output : 
# 2
# 


# Solution:


def minSwaps(arr):
	n = len(arr)
	arrpos = [*enumerate(arr)]
	arrpos.sort(key = lambda it : it[1])
	vis = {k : False for k in range(n)}
	ans = 0
	for i in range(n):
		if vis[i] or arrpos[i][0] == i:
			continue
		cycle_size = 0
		j = i
		while not vis[j]:
			vis[j] = True
			j = arrpos[j][0]
			cycle_size += 1
		if cycle_size > 0:
			ans += (cycle_size - 1)
	return ans
aa = input()
arr = [int(i) for i in input().split(" ")]
print(minSwaps(arr))