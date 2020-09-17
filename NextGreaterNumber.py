from itertools import permutations
n=input()
l=[]
for i in permutations(n):
    l.append(int("".join(i)))
l=sorted(l)
c=0
for i in range(len(l)):
    if int(n) == l[i]:
        c=i
print(l[c+1])
