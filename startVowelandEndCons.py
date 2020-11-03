from itertools import combinations
n=input().strip()
l=[]
for i in range(len(n)):
    for j in combinations(n,i+1):
        t = ''.join(list(j))
        if t[0] in 'aeiou' and t[-1] not in 'aeiou':
            l.append(t)
print(*sorted(set(l)))