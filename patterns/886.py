# QID: 886
# 
# In the IPL seasons valedictory function the organizers have organized for a dance program. The dance has to be performed by men along with the points of the diagonals of the square of side n and the females along with points of the borders. The remaining positions are filled by children. You have to determine their respective positions by writing a program.
# 
#  
# 
# Given an integer N indicates representing the matrix (N*N).where 1<=N<=100.
# 
# Print the N*N character matrix with the character F(Female), M(Male), C(Children).
# 
# Sample Input : 
# 7
# 
# Sample Output : 
# M F F F F F M
# F M C C C M F
# F C M C M C F
# F C C M C C F
# F C M C M C F
# F M C C C M F
# M F F F F F M
# 


# Solution:


def pattern(n):
    for i in range(n):
        l = []
        for j in range(n):
            if i == j or i+j == n-1:
                l.append('M')
            elif i == 0 or j == 0 or i == n-1 or j == n-1:
                l.append('F')
            else:
                l.append('C')
        print(*l)
        
n = int(input())
pattern(n)