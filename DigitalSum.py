n=list(map(int,input().strip()))#54321
t=sum(n)
if t>9:
    while t>9:
        l=list(str(t))
        r=[int(i) for i in l]
        t=sum(r)
    print(t)
else:
    print(t)
'''
Explanation: 
54321 = 5+4+3+2+1 = 15
15 = 5+1 = 6
hence 6<9
so 6 is the output
'''
