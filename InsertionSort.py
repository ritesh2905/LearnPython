a = [12,3,4,5,6,67,7,8,9,6,5,342,345,67]

for j in range(1,len(a)):
    key = a[j]
    i = j-1
    while i>=0 and a[i]>key:
        a[i+1] = a[i]
        i = i-1
    a[i+1] = key

print(a)
