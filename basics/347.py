# QID: 347
# 
# The Romans have attacked again. This time they are much more than the Persians but Shapur is ready to defeat them. He says: 'A lion is never afraid of a hundred sheep'.
# 
# Nevertheless Shapur has to find weaknesses in the Roman army to defeat them. So he gives the army a weakness number.
# 
# In Shapur's opinion the weakness of an army is equal to the number of triplets i, j, k such that i < j < k and ai > aj > ak where ax is the power of man standing at position x. The Roman army has one special trait — powers of all the people in it are distinct.
# 
# Help Shapur find out how weak the Romans are.
# 
# The first line of input contains a single number n, the number of men in Roman army. Next line contains n different positive integers powers of men in the Roman army.
# Input Size : N<=100000 
# Example:
# INPUT
# 3
# 3 2 1 
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
const int maxn = 1e6 + 10;

struct Node {
	ll val, front, rear;
} a[maxn], b[maxn];
ll ans;

void merge_sort(Node *A, int x, int y, Node *T) {
	if (y - x > 1) {
		int m = x + (y -x) / 2;
		int p = x, q = m, i = x;
		merge_sort(A, x, m, T);
		merge_sort(A, m, y, T);
		while (p < m || q < y) {
			if (q >= y || (p < m && A[p].val <= A[q].val)) {
				ans += A[p].front * (q - m);
				A[p].rear += (q - m);
				T[i++] = A[p++];
			}
			else {
				ans += A[q].rear * (m - p);
				A[q].front += (m - p);
				T[i++] = A[q++];
			}
		}
		for (i = x; i < y; i++)
			A[i] = T[i];
	}
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%lld", &a[i].val);
	ans = 0;
	merge_sort(a, 0, n, b);
	cout << ans << endl;
	return 0;
}