# QID: 355
# 
# Check whether the given 4 points form a square or not.
# Example:
# INPUT
# 10 10
# 10 20
# 20 20
# 20 10
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


class Point:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

def distSq(p, q):
	return (p.x - q.x) * (p.x - q.x) +\
		(p.y - q.y) * (p.y - q.y)

def isSquare(p1, p2, p3, p4):

	d2 = distSq(p1, p2) 
	d3 = distSq(p1, p3) 
	d4 = distSq(p1, p4) 
	if d2 == 0 or d3 == 0 or d4 == 0:
		return False

	if d2 == d3 and 2 * d2 == d4 and \
					2 * distSq(p2, p4) == distSq(p2, p3):
		return True

	if d3 == d4 and 2 * d3 == d2 and \
					2 * distSq(p3, p2) == distSq(p3, p4):
		return True

	if d2 == d4 and 2 * d2 == d3 and \
					2 * distSq(p2, p3) == distSq(p2, p4):
		return True

	return False

a,b = map(int, input().split(" "))
c,d = map(int, input().split(" "))
e,f = map(int, input().split(" "))
g,h = map(int, input().split(" "))
if __name__=="__main__":
	p1 = Point(a, b)
	p2 = Point(c, d)
	p3 = Point(e, f)
	p4 = Point(g, h)
	
	if isSquare(p1, p2, p3, p4):
		print('yes')
	else:
		print('no')