# t=int(input())
# for i in range(t):
#     n,m=map(int,input().split())
#     sum=0
#     for num in range(n,m+1):
#         if(num%2!=0):
#             sum=sum+num
#     print(sum)



def sum_odd(a,b):
    sum=0
    start=min(a,b)
    end=max(a,b)
    for i in range(start+1,end):
        if(i%2!=0):
            sum+=i
    return sum

t=int(input())
for n in range(t):
    a,b=map(int,input().split())
    r=sum_odd(a,b)
    print(r)
