x,y=map(int,input().split())
a=x
b=y
while(b!=0):
    r=a//b
    a=b
    b=r
gcd=a
print(gcd)


