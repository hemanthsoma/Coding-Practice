n=input()#500-5=2500
l=[];x=[];z=[]
for i in n:
    l.append(i[::])
    if i in '+-/*':
        break
first ="".join(l[0:len(l)-1])
fl = len(first)
for i in n[fl::]:
    x.append(i[::])
    if i in "=":
        break
second="".join(x[1:len(x)-1])
third=n[::-1]
for i in third:
    z.append(i[::])
    if i in '=':
        break
z=z[::-1]
output="".join(z[1:len(z)])
if int(first)*int(second)==int(output):
    print("*")
elif int(first)-int(second)==int(output):
    print("-")
elif int(first)+int(second)==int(output):
    print("+")
else:
    print("/")
