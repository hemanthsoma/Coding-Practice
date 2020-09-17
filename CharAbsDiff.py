n=set(input())
m=set(input())
c=0;d=0
for i in m:
    if i not in n:
        c+=1
    else:
        d+=1
for i in n:
    if i not in m:
        c+=1
print(abs(c-d))
