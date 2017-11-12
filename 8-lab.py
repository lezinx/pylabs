from random import randint


def output(m): 
	"""Вывод матрицы"""
	for i in range(n):
		for j in range(n):
			print(m[i][j], end = '\t')
		print()
	print()	

a = int(input('a: '))
b = int(input('b: '))
n = int(input('kvadr: '))
matrix = [[randint(a,b)for j in range(n)]for i in range(n)]
matrixCopy = []

for i in range(n):
	matrixCopy.append([])
	for j in range (n):
		matrixCopy[i].append(matrix[i][j])

output(matrix)

for k in range(n):
	matrix[k][0] = matrix[n - 1][k]
	matrix[n - 1][k] = matrixCopy[k][0]

output(matrix)
