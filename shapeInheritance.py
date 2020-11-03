from math import pi
if int(input())==1:
    t=float(input())
    print('%.2f'%(pi*(t*t)))
elif int(input())==2:
    g,k=map(float,input().split())
    print('%.2f'%(g*k))
else:
    h=float(input())
    print('%.2f'%(h*h))
