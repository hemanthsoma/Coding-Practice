n=int(input())
s=n
f=0;b=s-1;l=[[0 for _ in range(s)]for _ in range(s)]
g=n-(n//2)
while g!=0:
    for i in range(f,b+1):
        for j in range(f,b+1): 
            if i==f or i==b or j==f or j==b:
                l[i][j]=g
    f+=1;b-=1;g-=1
for i in l:
    print(*i,sep='')
'''
5
33333
32223
32123
32223
33333
'''