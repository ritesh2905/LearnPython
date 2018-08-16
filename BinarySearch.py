list = [1,2,3,4,5,6,7,8,9,10.11,12,13,14,15]
n = int(input('Enter the number: '))
#sort(list)
k=1
l = len(list)
m = int(l/2)
while(k<m):
    if list.index(m)>n:
        m=int(m/2)
        k += 1
    elif list.index(m)== n:
        print('Element found');
        break
    else:
        m = m//2
        k += 1
if(k==m):
    print('ELement not found')
    

    
