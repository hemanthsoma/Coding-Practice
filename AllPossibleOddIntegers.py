from itertools import permutations
n=input();l=[]
for i in permutations(n):
    t=int(''.join(list(i)))
    if t%2!=0:
        l.append(t)
print(*sorted(set(l)))
