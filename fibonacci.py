l = int(input('Limit: '))
a = 0
b = 1
print(a)
print(b)
for i in range(l-2):
    c = a+b
    print(i+2,':',c)
    a = b
    b = c
