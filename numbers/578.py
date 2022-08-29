# QID: 578
# 
# You are an employee of Rox Travel channel.The channel has decided to give allowances to some customer who satisfy these conditions. The conditions are:
# 
# The customer should be born on or before july 22 1987
# 
# The month of D.O.B month should be of 31 days.
# 
# You are given with the D.O.B of all the employees.Your task is to print the employee index who are having chance to avail special offer.
# 
# First line contains the number of employee.Next line contains an array of D.O.B of employees
# 
# Print the employee index (index at 1). Print-1 if there are no such employee
# 
# 
# Sample Input : 
# Input
# 4
# 23 MARCH 1996 23 MARCH 1986 22 JULY 1987 23 APRIL 1987
# 
# 
# Sample Output : 
# 2 3
# 
# 


# Solution:


def chunks(l, n = 3):
    for i in range(0, len(l), n):
        yield l[i: i+n]
a = int(input())
month_31 = ["JANUARY", "MARCH", "MAY", "JULY", "AUGUST", "OCTOBER", "DECEMBER"]
b = list(map(str,input().split()))
c = list(chunks(b))
for i in range(len(c)):
    c[i][1] = c[i][1].upper()
for i in range(len(c)):
    if (c[i][1] in month_31 and c[i][-1] <"1987"):
        c[i].insert(1,"#")
    if c[i][1] in month_31 and c[i][-1] == "1987":
        c[i].insert(1,"*")
ans = []
for i in range(len(c)):
    if "#" in c[i]:
        ans.append(i+1)
    elif "*" in c[i]:
        if c[i][2] in month_31[3] and int(c[i][0]) <= 22:
            ans.append(i+1)
        elif c[i][2] in month_31[:3]:
            ans.append(i+1)
print(*ans if ans != [] else "-1")