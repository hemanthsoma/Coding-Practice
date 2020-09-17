a,b,c=input().split(),0,0
for i in a:
    l=[int(x) for x in i.split('@')]
    b,c=b+l[0],c+l[1]
print('%.2f'%(b/c),'kmph')
