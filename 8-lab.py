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
length = int(input('kvadr: '))

matrix = [[randint(a,b)for j in range(length)]for i in range(length)]
output(matrix)

for k in range(length):
	temp = matrix[k][0]
	matrix[k][0] = matrix[length - 1][length - k - 1]
	matrix[length - 1][length - k - 1] = temp
output(matrix)

