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

for w in sorted(d, key=d.get, reverse=True):
  print( w,':',"'", d[w],"'")
