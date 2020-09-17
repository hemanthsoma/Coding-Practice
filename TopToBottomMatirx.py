n=int(input())
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(i,end=' ')
        i+=j
    print()
'''
5
1 6 10 13 15 
2 7 11 14 
3 8 12 
4 9 
5 

'''
