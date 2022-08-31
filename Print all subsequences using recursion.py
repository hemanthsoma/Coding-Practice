#code :

def fun(i,l,k,s):
	if i>=s:
		print(k)
		return
	k.append(l[i])
	fun(i+1,l,k,s)
	k.pop()
	fun(i+1,l,k,s)
l=[1,2,3,4]
fun(0,l,[],s=len(l))

#output :

[1, 2, 3, 4]
[1, 2, 3]
[1, 2, 4]
[1, 2]
[1, 3, 4]
[1, 3]
[1, 4]
[1]
[2, 3, 4]
[2, 3]
[2, 4]
[2]
[3, 4]
[3]
[4]
[]
