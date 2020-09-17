n=input()
m=input()
p=input()
z="".join(set(n+m))
p="".join(set(p))
if z==p:
    print("YES")
else:
    print("NO")
