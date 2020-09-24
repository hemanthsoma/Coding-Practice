n=[int(i) for i in input().strip()]
for i in range(len(n)):
    if n[i]%2!=0:
        n[i]=1
    elif n[i]%2==0:
        n[i]=0
s=0;c=0
for i in n[::-1]:
    s+=((2**c)*i)
    c+=1
print(s)
