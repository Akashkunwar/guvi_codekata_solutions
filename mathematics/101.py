# QID: 101
# 
# Given 2 numbers N and K.check if N is a power of K.Print 'yes' if it is a power of k otherwise print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# 64 8
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


def check_Power(N,k):
    if N <= 0 or k <=0:
        print("not a valid input")
    else:
        for i in range (1,20):
            x = k**i
            if x == N :
                print("yes")
                break
            elif x> N:
                print("no")
                break
j,l = map(int, input().split(" "))
check_Power(j,l)