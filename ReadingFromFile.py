file1 = open("article.txt", "r")
file2 = open("ignore.txt", "r")
file3 = open("new.txt", "a")
file1.seek(0,0)
file2.seek(0,0)
list1 = file1.readlines()
list2 = file2.readlines()
for i in list1:
    for j in list2:
        if i == j:
            file3.write(i)
            
