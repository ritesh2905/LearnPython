a = int(input('Enter: '))
b = int(input('Search: '))
n = a
count = 0
while n>0:
    if n%10 == b:
        count += 1
    n = n//10
print('Count is: ',count)
    
