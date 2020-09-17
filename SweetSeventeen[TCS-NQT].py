n=str(input())
t=''
for i in n:
    if i in 'ABCDEFGabcdefg':
        t=int(n,17)
    elif not t:
        t='Invalid'
print(t)
