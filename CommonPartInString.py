from difflib import SequenceMatcher
n=input()#mayday
m=input()#daybreak
p=SequenceMatcher(None,n,m)
t=p.find_longest_match(0,len(n),0,len(m))
print(n[t.a:t.a+t.size])
