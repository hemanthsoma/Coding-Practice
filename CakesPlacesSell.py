a,b,c = map(int,input().split())
if b-c>0 and a>=c:
    print(a+(b-c))
elif a==b or a==c or b==c:
    print(a)
else:
    print(-1)