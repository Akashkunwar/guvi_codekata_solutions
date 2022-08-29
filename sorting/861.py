# QID: 861
# 
# In <strong>Counting sort</strong>, the frequencies of distinct elements of the array to be sorted is counted and stored in an auxiliary array, by mapping its value as an index of the auxiliary array.
# 
# In counting sort,
# 
# <ul>
# 	<li>Take two arrays, Count[] and Result[] and given array is input[].</li>
# 	<li>Count[] will store the counts of each integer in the given array.</li>
# 	<li>Update the Count[] so that each index will store the sum till previous step. (Count[i]=Count[i] + Count[i-1]). Now updated Count[] array will reflect the actual position of each integer in Result[].</li>
# 	<li>Now navigate the input array taking one element at a time, Count[input[i]] will tell you the index position of input[i] in Result[]. When you do that, decrease the count in Count[input[i]] by 1.</li>
# 	<li>For Example:</li>
# </ul>
# 
# <img alt="" src="https://s3.ap-south-1.amazonaws.com/guvi-2.0/codekata/qid861.png" style="height:160px; width:350px" />
# 
# You have to sort the given array of integer values in counting sort manner.
# 
# Given an integer 'n' which indicates the length of array and followed by space separated ‘n’ integer values.Where 1<=n<=100 and 1<=A[i]<=10000.
# 
# Print the resultant sorted array by using counting sort method.where 1<=A[i]<=10000.
# 
# Sample Input : 
# 10
# 2 1 4 6 7 2 4 1 2 11
# 
# Sample Output : 
# 1 1 2 2 2 4 4 6 7 11
# 


# Solution:


a = input()
b = [int(i) for i in input().split()]
b = sorted(b)
print(*b)