import math
a,b,c,d=map(int,input().split())

left=b*math.log(a)
right=d*math.log(c)
if(left>right):
    print("YES")
elif(left<right):
    print("NO")
elif(left==right):
    print("NO")

# why not with direct power of a**b and c**d
# a,b,c,d=map(int,input().split())
# if(a**b>c**d):
#     print("YES")
# elif(a**b<c**d):
#     print("NO")
# elif(a**b==c**d):
#     print("NO")

# bcz in above program calculating power will overload hence
# time limit exceeded