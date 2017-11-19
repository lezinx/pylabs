import math

def NonRec(x, n):
	"""Iterative solution"""
	s = 1
	for i in range(1,n + 1):
		s += (i+1) * x ** i/math.factorial(i)
	return s

def Rec(x, n):
	"""Recursive solution"""
	if n == 0:
		return 1
	else:
		return x**n*(n+1)/math.factorial(n) + Rec(x, n - 1)

x = float(input('x = '))
while (x < -2.4 or x > 2.4):
	x = float(input('x = '))
epsilon = float(input('epsilon = '))
term = 1
n = 0
while(term > epsilon):
	term = term * x / (n + 1)
	n += 1
print('n = ', n)

y1 = NonRec(x, n)
y2 = Rec(x, n)
y3 = math.exp(x)*(x+1)
print('NonRec: ', y1)
print('Rec: ', y2)
print('Standard: ', y3)
print('Compare Standard with NonRec: ', y3 - y1)
print('Compare Standard with Rec: ', y3 - y2)