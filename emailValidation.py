from string import digits
n=input().split('@gmail.com')
n=''.join(n)
if n[:-1] and n[-1]=='_' or n[:-1] and n[:-1] and n[-1] in digits:
    print(True)
else:
    print(False)
