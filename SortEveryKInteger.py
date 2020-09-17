a,b=input().split()
l=list(map(int,input().split()))
a,b=int(a),int(b)
x=[sorted(l[i:i+b])[::-1] for i in range(0,len(l),b)]
for i in x:
    for j in i:
        print(j,end=" ")
