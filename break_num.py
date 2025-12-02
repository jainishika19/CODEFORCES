# t=int(input())
# num=list(map(int,input().split()))
# num=[18,24]
# count=0
# for n in num:
#     # for i in range(n):
#     while(n%2==0):
#         count+=1
#         n=n//2
# print(count)

def count(n):
    count=0
    
    while n%2==0:
        count+=1
        n=n//2
    return(count)

t=int(input())
num=list(map(int,input().split()))
ans=[]

for n in num:
    d=count(n)
    ans.append(d)
print(max(ans))