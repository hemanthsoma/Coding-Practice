l=list(map(int,input().split(',')))
f,s=l.index(5),l.index(8)
print(sum(l[:f]+l[s+1:])+int(''.join(list(map(str,l[f:s+1])))))
