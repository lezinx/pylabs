from random import randint


def output(m): 
	"""Вывод матрицы"""
	for i in range(length):
		for j in range(length):
			print(m[i][j], end = '\t')
		print()
	print()	

a = int(input('a: '))
b = int(input('b: '))
k = 0
z = 0
length = int(input('kvadr: '))

matrix = [[randint(a,b)for j in range(length)]for i in range(length)]
print(matrix)
output(matrix)

new = matrix[-1][1:]
new2 = []

print(new)
print(new2)
output(matrix)

