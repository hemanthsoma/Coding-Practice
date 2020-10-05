n=int(input());c=0
for i in range(n-1):
    for j in range(i,n-1):
        print('#',end='')
    print('H',end='')
    for j in range(i,0,-1):
        if j==i and i==1:
            print('OH',end='')
        elif j==i or i==n-2:
            print('O',end='')
        else:
            print('H',end='')
    for j in range(i-1):
        if j==i-2:
            print('OH',end='')
        elif i==n-2:
            print('O',end='')
        else:
            print('H',end='')
    print()
    c+=1
print('H'*(n+c),end='')
'''
input 
6

output
#####H
####HOH
###HOHOH
##HOHHHOH
#HOOOOOOOH
HHHHHHHHHHH
'''
