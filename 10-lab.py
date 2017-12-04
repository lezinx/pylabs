def dotproduct(a,b):
    return sum([a[i]*b[i] for i in range(len(a))])
a = [int(x) for x in input('a =').split()]
b = [int(x) for x in input('b =').split()]
print('Dot product:',dotproduct(a,b))