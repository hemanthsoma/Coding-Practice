from itertools import permutations
import string as s
n=input()
l=[]
for i in n:
    if i in s.digits:
        l.append(i)
l=''.join(set(l))
t=[]
for i in permutations(l):
    x=''.join(list(i))
    if x in '':
        break
    else:
        if int(x)%2==0:
            t.append(int(x))
        else:
            continue
if len(t)==0:
    print("-1")
else:
    print(max(t))
