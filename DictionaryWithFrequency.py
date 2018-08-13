# Dictionary of words with its frequency

s = input('Enter : ')
s = s.split(' ')

d = {}

for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
        d[i] = count

print(d)
    
        
    
