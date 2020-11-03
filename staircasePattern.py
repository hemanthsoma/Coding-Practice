n = int(input())
c = 0
l = []
for i in range(n//2):
    for j in range(i+1):
        c+=1
    l.append(c)
for i in l:
    if i>n:
        print(l.index(i))
        exit()

