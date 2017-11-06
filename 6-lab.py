# Задание 1
import math
n=int(input('Введіть значення n=')) 
summa=0
for i in range(1,n+1):
	 summa=summa+math.sin(i)+math.cos(i)
print('summa=',summa)

# Задание 2
def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax
a = [int(x) for x in input('Введіть N = ').split()]
print (highestNumber(a))
