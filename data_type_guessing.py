# my code 
# n,k,a=map(int,input().split())
# r=(n*k)/a
# if(r>= -2147483648 and r<=2147483647):
#     print("int")
# elif(r>2147483647):
#     print("long long")
# elif(type(r)==float):
#     print("double")

# right code 
n,k,a=map(int,input().split())
value=(n*k)/a
if(value!=int(value)):
    print("double")
else:
    value=int(value)
    if value>= -2147483648 and value<=2147483647:
        print("int")
    else:
        print("long long")


