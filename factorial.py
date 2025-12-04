t=int(input())
for i in range(t):
    n=int(input())
    factorial=1
    while(n>0):
        factorial=factorial*n
        n-=1
    print(factorial)
    