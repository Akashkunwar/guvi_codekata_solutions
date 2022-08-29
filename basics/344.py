# QID: 344
# 
#  Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), if it is not possible to select coins in such a way that they sum up to S then print '-1'.
# Example: Given coins with values 1, 3, and 5. And the sum S is 11.
# Output: 3, 2 coins of 3 and 1 coin of 5
# Input Size : N<=10000 
# Example:
# INPUT
# 3 11
# 1 3 5
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


import sys
def minCoins(coins, m, V):
	if (V == 0):
		return 0
	res = sys.maxsize
	for i in range(0, m):
		if (coins[i] <= V):
			sub_res = minCoins(coins, m, V-coins[i])
			if (sub_res != sys.maxsize and sub_res + 1 < res):
				res = sub_res + 1
	return res
u,V = map(int,input().split(" "))
coins = [int(i) for i in input().split(" ")]
m = len(coins)
print(minCoins(coins, m, V))