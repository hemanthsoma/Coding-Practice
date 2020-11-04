n,m=map(int,input().split())
l=[];t=n
for j in range(4):
    p=[]
    for i in range(4):
        p.append(t)
        t+=m
    l.append(p)
t_m = zip(*l)
k=0
for i in t_m:
    for j in range(len(i)):
        print(i[j]*l[k][j],end=' ')
    print()
    k+=1

'''
Input 
3 5
Output
9 184 559 1134 
184 784 1584 2584 
559 1584 2809 4234 
1134 2584 4234 6084
'''
