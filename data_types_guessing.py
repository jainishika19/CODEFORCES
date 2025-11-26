n,k,a=map(int,input().split())
result=(n*k)/a
# if(result.isinteger()):
#     print("int")
if isinstance(result,int):
    print("int")
elif isinstance(result,float):
    print("double")
# if isinstance(result,int):
#     printz("int")