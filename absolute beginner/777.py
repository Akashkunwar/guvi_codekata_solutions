# QID: 777
# 
# You will be provided with a number. Print the number of days in the month corresponding to that number.
# 
# Note: In case the input is February, print 28 days. If the Input is not in valid range print &quot;Error&quot;.
# 
# The input is in the form of a number. 
# 
# Find the days in the month corresponding to the input number.
# Print Error if the input is not in a valid range.
# 
# Sample Input : 
# 8
# 
# Sample Output : 
# 31
# 


# Solution:


num = input()
if (num =="1"):
    print("31")
elif (num =="2"):
    print("28")
elif (num =="3"):
    print("31")
elif (num =="4"):
    print("30")
elif (num =="5"):
    print("31")
elif (num =="6"):
    print("30")
elif (num =="7"):
    print("31")
elif (num =="8"):
    print("31")
elif (num =="9"):
    print("30")
elif (num =="10"):
    print("31")
elif (num =="11"):
    print("30")
elif (num =="12"):
    print("31")
else:
    print("Error")