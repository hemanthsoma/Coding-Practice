n=int(input())
l=list(map(int,input().split()))
res = ["Band 0-10:","Band 11-20:","Band 21-30:","Band 31-40:","Band 41-50:","Band 51-60:","Band 61-70:","Band 71-80:","Band 81-90:","Band 91-100:"]
a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0
for i in l:
    if i>=0 and i<=10:
        a+=1
res[0]+=' '+str(a)
print(res)
