a = [10,20,40,50,30,90,80,70,100,60]

for i in range(1,len(a)-1):
    min = i
    for j in range(i+1,len(a)):
        if a[min]>a[j]:
            min = j
    if a[i]>a[min]:
        temp = a[i]
        a[i] = a[min]
        a[min] = temp

print(a)
