n=input()
r=int(n)*2-3
f=n;s=n;c=n;t=1;l=[]
for i in range(int(n)):
    if f[-1]=='1':
        print(f+c*r+s[1:])
    else:
        z=f+c*r+s
        print(z);l.append(z)
    f=f+str(int(n)-t);s=str(int(n)-t)+s
    c=str(int(n)-t);t+=1;r-=2
for i in l[::-1]:print(i)
'''
5
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
'''
