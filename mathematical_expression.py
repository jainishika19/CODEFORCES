a,s,b,c,d=input().split()
a=int(a)
b=int(b)
d=int(d)
addition=a+b
subtraction=a-b
multiplication=a*b 

if(s=="+"):
    print("Yes" if d==addition else a+b)
elif(s=="-"):
    print("Yes" if d==subtraction else a-b)
elif(s=="*"):
    print("Yes" if d==multiplication else a*b)


