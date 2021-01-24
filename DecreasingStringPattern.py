n=input()
print(n)
c=1;l=len(n)//2-1;d=0;g=len(n)//2+1
for i in range(len(n)//2-1):
    print('*'*c+n[d:l]+n[g:len(n)]+'*'*c)
    l-=1;c+=1;g+=1
print('*'*len(n))
'''
barber
barber
*baer*
**br**
******
'''
