n='12345' #input any int as a string
X=2 
j="".join(n[-X:])
s=0
for i in j:
    s=s+int(i)
print(s)
