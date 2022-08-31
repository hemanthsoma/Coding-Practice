#code :

def fun(i,l,k,s,su,c):
	if i>=s:
		if c==su:
		   print(k)
		return
	k.append(l[i])
	c+=l[i]
	fun(i+1,l,k,s,su,c)
	k.pop()
	c-=l[i]
	fun(i+1,l,k,s,su,c)
l=[1,2,3,4]
su=6
s=len(l)
c=0
fun(0,l,[],s,su,c)



#output :

[1, 2, 3]
[2, 4]
