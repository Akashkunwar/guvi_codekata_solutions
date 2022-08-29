# QID: 780
# 
# You are given with <strong>Principle amount($)</strong>,<strong> Interest Rate(%) </strong>and <strong>Time (years)</strong> in that order. Find <em><strong>Simple Interest</strong></em>.
# 
# Print the output up to two decimal places (Round-off if necessary).
# 
# <strong><em>(S.I. = P*T*R/100)</em></strong>
# 
# Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.
# 
# Find the Simple interest and print it up to two decimal places. Round off if required.
# 
# Sample Input : 
# 1000 2 5
# 
# Sample Output : 
# 100.00
# 


# Solution:


p,r,t = map(float, input().split(" "))
n = p*r*t/100
formatted_float = "{:.2f}".format(n)
print(formatted_float)