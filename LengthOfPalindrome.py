n=input()
while n[::]==n[::-1]:
    print(len(n))
    break
else:
    d=int(n)+int(n[::-1])
    n=d    
