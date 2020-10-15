n=int(input())
l=[i for i in range(1,n+1)]
m=n
while(m>=1):
    g=[l[i:i+m] for i in range(0,len(l),m)]
    for i in g:
        print('(',end='')
        for k in i:
            if k==m or k==n or k%m==0:
                print(str(k),end='') 
            else:
                print(str(k),end=' ')
        print(')',end='')
    print()
    m-=1
'''
Input 
5

Output 
(1 2 3 4 5)
(1 2 3 4)(5)
(1 2 3)(4 5)
(1 2)(3 4)(5)
(1)(2)(3)(4)(5)
'''
