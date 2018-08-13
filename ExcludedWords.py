#Displaying non execluded words in a sentence
exwords = ['and','or','a','is','this','that','not','an']
s = input('Enter: ')
s = s.split(' ')
s = set(s)
k = []

for i in s:
    count = 0
    for j in exwords:
        if i==j:
            count +=1
    if count == 0:
        k.append(i)

print(k)    
    
