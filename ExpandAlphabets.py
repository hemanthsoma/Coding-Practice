import re
m=re.split('(\d+)',input().strip())                     =
for i in range(0,len(m)-1,2):
    if i%2==0:
        print(m[i]*int(m[i+1]),end="")
