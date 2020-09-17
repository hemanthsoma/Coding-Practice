n=input()
m=[str(int(n[i])**2) for i in range(1,len(n),2)]
m=''.join(m)[:4]
if len(m)!=4:
    print("-1")
else:
    print(m)
