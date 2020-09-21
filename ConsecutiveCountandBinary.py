n=int(input())
n=str(bin(n)[2:])
m=n.split('1')
l=[];y=[]
for i in m:
    if len(i)==0:
        pass
    else:
        l.append(str(len(i))*len(i))
        y.append(len(i))
l=[int(i) for i in l]
for i in range(len(l)):
    n=n.replace('0'*y[i],str(l[i]))
print(bin(int(n))[2:])
'''
input 1
25
output 1
10101111010101

input 2
274
output 2
111111100100010111011010011


Explanation 

Binary of 274 is 0b100010010 - 100010010
To replace number of consecutive count of 0's in binary of 274
Then, 100010010 - 133312211
Output - binary of 133312211 - 111111100100010111011010011


'''
