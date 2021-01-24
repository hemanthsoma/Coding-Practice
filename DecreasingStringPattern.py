n=input()
c=0;d=0;l=len(n)//2;g=l
for i in range(len(n)//2+1):
    print('*'*c+n[d:l]+n[g:len(n)]+'*'*c)
    l-=1;c+=1;g+=1
'''
barber
barber
*baer*
**br**
******
'''
