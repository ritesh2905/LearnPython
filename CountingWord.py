s = input('Enter: ')
f = input('Word: ')
s = s.split(' ')
count = 0
for i in s:
    if s[i] == f:
        count += 1;

print('Count: ',count)
    
