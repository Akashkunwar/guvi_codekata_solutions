# QID: 289
# 
# Given an arraylist A of string type which has name#mark1#mark2#mark3 format. Retrieve the name of the student who has scored max marks(total of three).
# for eg: input: {'arun#12#12#12','deepak#13#12#12'}
# output: Deepak 
# Input Size : A <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# arun#12#12#12
# deepak#13#12#12
# OUTPUT
# deepak
# 
# 
# 
# 


# Solution:


a = [i for i in input().split('#')]
b = [i for i in input().split('#')]

am = 0
for x in a:
  if x.isdigit():
    am = am + int(x)

bm = 0
for x in b:
  if x.isdigit():
    bm = bm + int(x)

if am>bm:
  print(a[0])
else:
  print(b[0])