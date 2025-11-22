num=int(input())
a=num//10
b=num%10
# check divisibility but avoid division by zero
# when a/b-- b!=0
# when b/a-- a!=0
if(a!=0 and b%a==0):
    print("YES")
elif(b!=0 and a%b==0):
    print("YES")
else:
    print("NO")
