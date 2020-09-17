n=input()
l=list(map(int,input().split()))
m=len(n)+l[1]
p=n*(m//len(n))
if p[l[0]-1]==p[l[1]-1]:
    print("YES")
else:
    print("NO")
