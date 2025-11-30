age=int(input())
Y=age//365
M=(age-365*Y)//30
D=(age-(365*Y+M*30))
print(Y,"years")
print(M,"months")
print(D,"days")