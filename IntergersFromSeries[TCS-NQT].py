n=int(input())
l=list(map(int,input().split()))
for i in range(0,10001):
    r=[]
    t=(2**i)+1
    r.append(t)
for i in l:
    if i in r:
        print(i,end=' ')
