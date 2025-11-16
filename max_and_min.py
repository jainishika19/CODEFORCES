a,b,c=map(int,input().split())
# print(a if a<b and a<c else b if b<c and b<a else c,a if a>b and a>c else b if b>c and b>a else c
minimum=min(a,b,c)
maximum=max(a,b,c)
print(minimum,maximum)

