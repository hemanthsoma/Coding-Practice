n=int(input())
l=list(map(int,input().split()))
for i in l:
    if l.count(i)==len(l):
        print(i,end=' ')
    elif i%2==0:
        evenSum=0
        for j in l:
            if i==j:
                evenSum+=i
                continue
            else:
                s = str(j)
                for r in s:
                    r = int(r)
                    if r%2==0:
                        evenSum+=r
        print(evenSum,end=' ')
        evenSum=0
    elif i%2!=0:
        oddSum=0
        for j in l:
            if i==j:
                oddSum+=i
                continue
            else:
                s = str(j)
                for r in s:
                    r = int(r)
                    if r%2!=0:
                        oddSum+=r
        print(oddSum,end=' ')
        oddSum=0

'''
Input 
4 
32 25 16 71

Output
40 37 20 80
'''
