a,s,b=input().split()
a=int(a)
b=int(b)
if(s=="<"):
    print("Right" if a<b else "Wrong")
elif(s==">"):
    print("Right" if a>b else "Wrong")
elif(s=="="):
    print("Right" if a==b else "Wrong")