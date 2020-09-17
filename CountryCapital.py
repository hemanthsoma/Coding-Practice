n=int(input())
l=[]
for i in range(n):
    l.append(input().split())
m=input()
t=0
for i in l:
    for j in range(len(i)):
        if m==i[j]:
            t=i[j+1]
    else:
        t="NONE"
print(t)
