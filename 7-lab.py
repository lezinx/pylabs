import random
# Завдання 1a),1b)
k = int(input('Введите k = '))
m = int(input('Введите m = '))
for i in range(1,m + 1):
	print(random.randint(13,900),end = ' ') #1a)
	if i % k == 0:
		print()		
print()


k = int(input('Введите k = '))
m = int(input('Введите m = '))
for i in range(1,m + 1):
	print(round(random.uniform(-1,1),2),end = ' ') #2b)
	if i % k == 0:
		print()		
print()

# Завдання 2a),2b)

def higher_than_c(comp):
	"""Функція для виведення к-сті елементів більших за С"""
	compare = comp[0]
	a = 0
	for k in range(n):
		if comp[k] > c:
			a += 1
	print(a)


def dobutok(array):
	"""Функція для виведення добутку чисел після максимального елемента за модулем"""
	k = [abs(number) for number in array]
	maxID = k.index(max(k))
	dob = 1
	for l in range(maxID + 1, len(k)):
		dob = dob * k[l]
		
	print(dob)


a = int(input('Vvedite a: '))
b = int(input('Vvedite b: '))
n = int(input('Vvedite n: '))
if a < b:
	N = [random.randint(a,b) for i in range(n)]
	print(N)
	c = int(input('Vvedite c: '))
	higher_than_c(N)
	dobutok(N)

