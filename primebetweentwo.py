a = int(input('Enter 1st: '))
b = int(input('Enter 2nd: '))
c= []
for i in range(a,b):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count += 1
            break
    if count == 0:
        print(i)

