s = input('Enter: ')
s = s.split()
l = []

for i in s:
    l.append(len(i))

k = l.index(max(l))
print(s[k])
