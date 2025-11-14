import math
a,b=map(int,(input().split()))
print("floor",a ,"/", b ,"=",math.floor(a/b))
print("ceil", a,"/",b, "=",math.ceil(a/b))
print("round",a,"/",b, "=",math.floor(a/b+0.5)) #if we use round fntn here then it rounds
# to even number i.e. 2
# 10/4=2.55=2(for round)
# 10/4=2.55=3(by above )
