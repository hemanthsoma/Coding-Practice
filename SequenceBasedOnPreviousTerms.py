n=int(input())
print(n,end=' ')
while n!=1:
    if n%2!=0:
        print((n*3)+1,end=' ')
        n = (n*3)+1
    else:
        print(n//2,end=' ')
        n = n//2

'''
Input 
13
Output
13 40 20 10 5 16 8 4 2 1
'''
