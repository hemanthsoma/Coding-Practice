from functools import lru_cache

@lru_cache(maxsize=1000)
def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibo(n-1)+fibo(n-2)

for n in range(1,100):
    print(fibo(n),end=' ')
