n=int(input())
for i in range(1,n+1):
    c=i;d=n-i+1
    for j in range(1,i+1):
        if j%2!=0:
            print(c,end=' ')
            c+=n-j
        else:
            print(d,end=' ')
            c+=n-j
        d+=n-j+1
    print()
'''
5
1 
2 9 
3 8 10 
4 7 11 14 
5 6 12 13 15
'''