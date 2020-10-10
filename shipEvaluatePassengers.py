n=int(input())
l=[]
for i in range(n):
    l.append(input().split())
m=int(input());c=0;d=0;e=0
for i in range(n):
    if l[i][1] == 'children':
        c+=1
    elif l[i][1] == 'men':
        d+=1 
    elif l[i][1] == 'women':
        e+=1
t = max(c,e,d)
print(t,m-t,0)
