#a)
a_input = input('Write something: ');
b = a_input.index(':');
print(a_input[b+1:]);
#b)
b_input = input('Write something: ').split('. ');
print(b_input);
res = 0;
for i in range(len(b_input)):
    if b_input[i].count(' ') % 2 ==0:
        res += 1
print(res);
#c)
# s = input("Write something: ").split(',')
# print(s[0])
s = input("Write something")
print(s.partition(",")[0])


